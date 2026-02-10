from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_admin
from app.services.instagram_service import InstagramService

router = APIRouter()

@router.post("/sync")
def sync_instagram(db: Session = Depends(get_db), _admin=Depends(require_admin)):
    return InstagramService.sync_latest(db)
