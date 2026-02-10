from datetime import datetime, timedelta, time
from sqlalchemy.orm import Session
from app.models.service import Service
from app.models.booking import Booking, BookingStatus

SALON_OPEN = time(10, 0)
SALON_CLOSE = time(21, 0)

class SlotService:
    @staticmethod
    def generate_slots(db: Session, date_str: str, service_id: int, staff_id: int | None):
        # date_str: "YYYY-MM-DD"
        day = datetime.fromisoformat(date_str).date()

        service = db.query(Service).filter(Service.id == service_id, Service.is_active == True).first()
        if not service:
            return []

        duration = timedelta(minutes=service.duration_minutes)

        start_dt = datetime.combine(day, SALON_OPEN)
        end_dt = datetime.combine(day, SALON_CLOSE)

        # pull existing bookings for date (+ staff if provided)
        q = db.query(Booking).filter(
            Booking.status != BookingStatus.cancelled,
            Booking.starts_at >= start_dt,
            Booking.starts_at < end_dt
        )
        if staff_id:
            q = q.filter(Booking.staff_id == staff_id)

        bookings = q.all()

        def overlaps(a_start, a_end, b_start, b_end):
            return a_start < b_end and a_end > b_start

        slots = []
        cur = start_dt
        while cur + duration <= end_dt:
            candidate_start = cur
            candidate_end = cur + duration

            conflict = any(overlaps(candidate_start, candidate_end, b.starts_at, b.ends_at) for b in bookings)
            if not conflict:
                slots.append({
                    "starts_at": candidate_start.isoformat(),
                    "ends_at": candidate_end.isoformat()
                })
            cur += timedelta(minutes=15)  # 15-min interval grid
        return slots
