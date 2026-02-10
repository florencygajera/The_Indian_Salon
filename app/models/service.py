from sqlalchemy import Column, Integer, String, Numeric, Boolean
from app.db.base import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    category = Column(String(80), nullable=False)  # Hair, Grooming, Skin, Nails, Makeup
    price = Column(Numeric(10, 2), nullable=False, default=0)
    duration_minutes = Column(Integer, nullable=False, default=30)
    is_active = Column(Boolean, default=True)
