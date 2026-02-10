from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_admin: bool
    is_active: bool

    class Config:
        from_attributes = True

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
