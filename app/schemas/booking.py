from pydantic import BaseModel
from datetime import datetime

class SlotOut(BaseModel):
    starts_at: datetime
    ends_at: datetime
    remaining_capacity: int
    is_full: bool

class BookingCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: str | None = None
    service_id: int
    staff_id: int | None = None
    starts_at: datetime
    ends_at: datetime
    notes: str | None = None
