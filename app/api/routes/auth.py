from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import TokenOut
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/login", response_model=TokenOut)
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    token = AuthService.login(db, email, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"access_token": token, "token_type": "bearer"}
