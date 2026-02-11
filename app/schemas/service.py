from pydantic import BaseModel, Field

class ServiceOut(BaseModel):
    id: int
    name: str
    category: str
    duration_minutes: int
    active: bool
    max_per_slot: int

    class Config:
        from_attributes = True


class ServiceOut(BaseModel):
    id: int
    name: str
    category: str
    active: bool = True
    duration_minutes: int
    is_active: bool
    max_per_slot: int

    class Config:
        from_attributes = True

   