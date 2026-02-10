from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.core.security import decode_token
from app.repositories.user_repo import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    email = decode_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user_by_email(db, email)
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def require_admin(user = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")
    return user
