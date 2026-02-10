from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
import enum

class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)

    customer_name = Column(String(120), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    customer_email = Column(String(180), nullable=True)

    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable=True)

    starts_at = Column(DateTime(timezone=True), nullable=False, index=True)
    ends_at   = Column(DateTime(timezone=True), nullable=False, index=True)

    status = Column(Enum(BookingStatus), default=BookingStatus.pending, nullable=False)
    notes = Column(String(500), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    service = relationship("Service")
    staff = relationship("Staff")
