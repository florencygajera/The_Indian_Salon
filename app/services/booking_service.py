from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.booking import Booking, BookingStatus


class BookingService:
    @staticmethod
    def check_slot_availability(db: Session, service_id: int, starts_at, max_per_slot: int = 1):
        """Check if a slot is available for booking."""
        booked = db.query(Booking).filter(
            Booking.service_id == service_id,
            Booking.starts_at == starts_at,
            Booking.status != BookingStatus.cancelled
        ).count()
        
        remaining = max_per_slot - booked
        is_full = remaining <= 0
        
        return {
            "booked": booked,
            "remaining": remaining,
            "is_full": is_full
        }

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
