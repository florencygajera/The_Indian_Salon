from sqlalchemy.orm import Session
from app.schemas.booking import BookingCreate
from app.models.booking import Booking, BookingStatus
from app.repositories.booking_repo import find_conflict

class BookingService:
    @staticmethod
    def create_booking(db: Session, data: BookingCreate):
        if data.staff_id:
            conflict = find_conflict(db, data.staff_id, data.starts_at, data.ends_at)
            if conflict:
                raise ValueError("Slot already booked for this staff member.")

        booking = Booking(
            customer_name=data.customer_name,
            customer_phone=data.customer_phone,
            customer_email=data.customer_email,
            service_id=data.service_id,
            staff_id=data.staff_id,
            starts_at=data.starts_at,
            ends_at=data.ends_at,
            status=BookingStatus.pending,
            notes=data.notes
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
