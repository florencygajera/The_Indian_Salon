from sqlalchemy.orm import Session
from app.models.service import Service

def list_services(db: Session, active_only: bool = True):
    q = db.query(Service)
    if active_only:
        q = q.filter(Service.active == True)
    return q.order_by(Service.category.asc(), Service.name.asc()).all()
