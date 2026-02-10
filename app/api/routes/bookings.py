from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.booking import BookingCreate, BookingOut
from app.services.booking_service import BookingService
from app.services.email_service import EmailService
from app.services.whatsapp_service import WhatsAppService
from app.services.slot_service import SlotService

router = APIRouter()

@router.get("/slots")
def get_slots(date: str, service_id: int, staff_id: int | None = None, db: Session = Depends(get_db)):
    return SlotService.generate_slots(db, date, service_id, staff_id)

@router.post("/", response_model=BookingOut)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    try:
        booking = BookingService.create_booking(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

    # Notifications (safe if not configured; they simply skip)
    EmailService.send_new_booking(booking)
    WhatsAppService.send_new_booking(booking)

    return booking
