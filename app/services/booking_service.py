from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.booking import Booking, BookingStatus

class BookingService:
    @staticmethod
    def create_booking(db: Session, data):
        # Basic overlap check (works in any DB; Postgres constraint is still recommended)
        if data.staff_id:
            conflict = db.query(Booking).filter(
                Booking.staff_id == data.staff_id,
                Booking.status != BookingStatus.cancelled,
                and_(Booking.starts_at < data.ends_at, Booking.ends_at > data.starts_at)
            ).first()
            if conflict:
                raise ValueError("Slot already booked for this staff member.")

        booking = Booking(**data.model_dump())
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
