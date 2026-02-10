from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_admin
from app.schemas.service import ServiceCreate, ServiceOut
from app.models.service import Service
from app.repositories.service_repo import list_services, create_service

router = APIRouter()

@router.get("/", response_model=list[ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return list_services(db, active_only=True)

@router.post("/", response_model=ServiceOut)
def add_service(payload: ServiceCreate, db: Session = Depends(get_db), _admin=Depends(require_admin)):
    obj = Service(**payload.model_dump())
    return create_service(db, obj)
