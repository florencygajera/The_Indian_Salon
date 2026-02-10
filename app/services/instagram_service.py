from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc
import requests

from app.core.config import settings
from app.models.instagram_media import InstagramMedia

GRAPH = "https://graph.facebook.com/v19.0"

class InstagramService:
    @staticmethod
    def sync_latest(db: Session) -> dict:
        """
        Pull latest IG media and cache in DB.
        Requires IG_USER_ID + IG_ACCESS_TOKEN (Graph API).
        """
        if not (settings.IG_USER_ID and settings.IG_ACCESS_TOKEN):
            return {"synced": 0, "skipped": True, "reason": "IG_USER_ID / IG_ACCESS_TOKEN not configured"}

        fields = "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp"
        limit = settings.IG_SYNC_LIMIT

        url = f"{GRAPH}/{settings.IG_USER_ID}/media"
        params = {
            "fields": fields,
            "limit": limit,
            "access_token": settings.IG_ACCESS_TOKEN,
        }

        r = requests.get(url, params=params, timeout=20)
        data = r.json()

        if r.status_code != 200:
            return {"synced": 0, "error": data}

        items = data.get("data", [])
        synced = 0

        for it in items:
            ig_id = it.get("id")
            if not ig_id:
                continue

            existing = db.query(InstagramMedia).filter(InstagramMedia.ig_media_id == ig_id).first()
            if existing:
                # Update in case caption/url changed
                existing.media_type = it.get("media_type") or existing.media_type
                existing.media_url = it.get("media_url")
                existing.thumbnail_url = it.get("thumbnail_url")
                existing.permalink = it.get("permalink") or existing.permalink
                existing.caption = it.get("caption")
                ts = it.get("timestamp")
                existing.timestamp = datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else existing.timestamp
            else:
                ts = it.get("timestamp")
                db.add(InstagramMedia(
                    ig_media_id=ig_id,
                    media_type=it.get("media_type") or "IMAGE",
                    media_url=it.get("media_url"),
                    thumbnail_url=it.get("thumbnail_url"),
                    permalink=it.get("permalink") or "",
                    caption=it.get("caption"),
                    timestamp=datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None,
                    is_active=True
                ))
                synced += 1

        db.commit()
        return {"synced": synced, "received": len(items), "ok": True}

    @staticmethod
    def get_gallery(db: Session, limit: int | None = None):
        limit = limit or settings.IG_SYNC_LIMIT
        return (db.query(InstagramMedia)
                .filter(InstagramMedia.is_active == True)
                .order_by(desc(InstagramMedia.timestamp), desc(InstagramMedia.id))
                .limit(limit)
                .all())
