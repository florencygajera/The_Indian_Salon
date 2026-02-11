from pydantic import BaseModel, Field

class ServiceCreate(BaseModel):
    name: str
    category: str
    duration_minutes: int = 30
    is_active: bool = True
    max_per_slot: int = Field(default=1, ge=1, le=50)

class ServiceOut(BaseModel):
    id: int
    name: str
    category: str
    duration_minutes: int
    is_active: bool
    max_per_slot: int

    class Config:
        from_attributes = True
