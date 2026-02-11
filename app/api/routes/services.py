from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.service import ServiceOut
from app.repositories.service_repo import list_services

router = APIRouter()

@router.get("/", response_model=list[ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return list_services(db, active_only=True)
