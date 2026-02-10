from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class BookingCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[EmailStr] = None
    service_id: int
    staff_id: Optional[int] = None
    starts_at: datetime
    ends_at: datetime
    notes: Optional[str] = None

class BookingOut(BaseModel):
    id: int
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = None
    service_id: int
    staff_id: Optional[int] = None
    starts_at: datetime
    ends_at: datetime
    status: str
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class SlotQuery(BaseModel):
    date: str  # "YYYY-MM-DD"
    service_id: int
    staff_id: Optional[int] = None
