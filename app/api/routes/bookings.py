from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, date, time, timedelta
from app.api.deps import get_db
from app.models.booking import Booking, BookingStatus
from app.models.service import Service
from app.schemas.booking import SlotOut, BookingCreate

router = APIRouter()

def build_slots(d: date, duration_min: int):
    # salon working hours (change if needed)
    start = datetime.combine(d, time(10, 0))
    end   = datetime.combine(d, time(21, 0))

    slots = []
    cur = start
    step = timedelta(minutes=duration_min)
    while cur + step <= end:
        slots.append((cur, cur + step))
        cur += step
    return slots

@router.get("/slots", response_model=list[SlotOut])
def get_slots(
    date: str = Query(...),
    service_id: int = Query(...),
    db: Session = Depends(get_db)
):
    try:
        d = datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    service = db.query(Service).filter(Service.id == service_id, Service.active == True).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    slots = build_slots(d, service.duration_minutes)

    results: list[SlotOut] = []
    for (s, e) in slots:
        count = (
            db.query(Booking)
            .filter(
                Booking.service_id == service_id,
                Booking.starts_at == s,
                Booking.ends_at == e,
                Booking.status != BookingStatus.cancelled
            )
            .count()
        )

        remaining = max(service.max_per_slot - count, 0)
        results.append(SlotOut(
            starts_at=s,
            ends_at=e,
            remaining_capacity=remaining,
            is_full=(remaining == 0)
        ))
    return results


@router.post("/", status_code=201)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == payload.service_id, Service.active == True).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    # count existing bookings for that exact slot
    count = (
        db.query(Booking)
        .filter(
            Booking.service_id == payload.service_id,
            Booking.starts_at == payload.starts_at,
            Booking.ends_at == payload.ends_at,
            Booking.status != BookingStatus.cancelled
        )
        .count()
    )

    if count >= service.max_per_slot:
        raise HTTPException(status_code=409, detail="Slot is full. Please select another slot.")

    b = Booking(
        customer_name=payload.customer_name,
        customer_phone=payload.customer_phone,
        customer_email=payload.customer_email,
        service_id=payload.service_id,
        staff_id=payload.staff_id,
        starts_at=payload.starts_at,
        ends_at=payload.ends_at,
        notes=payload.notes,
        status=BookingStatus.pending
    )
    db.add(b)
    db.commit()
    db.refresh(b)
    return {"ok": True, "booking_id": b.id}
