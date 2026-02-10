from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    category: str
    price: float
    duration_minutes: int
    is_active: bool = True

class ServiceOut(ServiceCreate):
    id: int
    class Config:
        from_attributes = True
