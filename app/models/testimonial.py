from sqlalchemy import Column, Integer, String, Integer
from app.db.base import Base

class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(120), nullable=False)
    rating = Column(Integer, nullable=False, default=5)
    message = Column(String(600), nullable=False)
