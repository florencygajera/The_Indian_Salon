from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.user import User

def seed_admin(db: Session, email: str, password: str, full_name: str = "Admin"):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        return existing

    admin = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        is_admin=True,
        is_active=True,
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin
