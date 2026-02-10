from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime
from app.models.booking import Booking, BookingStatus

def find_conflict(db: Session, staff_id: int, starts_at: datetime, ends_at: datetime):
    return db.query(Booking).filter(
        Booking.staff_id == staff_id,
        Booking.status != BookingStatus.cancelled,
        and_(Booking.starts_at < ends_at, Booking.ends_at > starts_at)
    ).first()

def list_bookings(db: Session, limit: int = 50):
    return (
        db.query(Booking)
        .order_by(Booking.created_at.desc())
        .limit(limit)
        .all()
    )
