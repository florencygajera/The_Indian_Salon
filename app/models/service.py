from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    category = Column(String(60), nullable=False)
    duration_minutes = Column(Integer, nullable=False, default=30)

    active = Column(Boolean, default=True, nullable=False)
    max_per_slot = Column(Integer, default=1, nullable=False)
