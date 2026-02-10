from sqlalchemy import Column, Integer, String, DateTime, Boolean, UniqueConstraint
from sqlalchemy.sql import func
from app.db.base import Base

class InstagramMedia(Base):
    __tablename__ = "instagram_media"

    id = Column(Integer, primary_key=True)
    ig_media_id = Column(String(80), nullable=False)
    media_type = Column(String(30), nullable=False)      # IMAGE, VIDEO, CAROUSEL_ALBUM
    media_url = Column(String(500), nullable=True)       # image/video url
    thumbnail_url = Column(String(500), nullable=True)   # for videos
    permalink = Column(String(500), nullable=False)
    caption = Column(String(2200), nullable=True)
    timestamp = Column(DateTime(timezone=True), nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint("ig_media_id", name="uq_ig_media_id"),)
