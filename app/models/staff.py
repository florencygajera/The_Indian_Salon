from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    role = Column(String(80), nullable=True)
    active = Column(Boolean, default=True)
