from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_admin
from app.repositories.booking_repo import list_bookings
from app.repositories.service_repo import list_services

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def admin_login_page(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db), _admin=Depends(require_admin)):
    bookings = list_bookings(db, limit=20)
    services = list_services(db, active_only=False)
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "bookings": bookings,
        "services": services
    })

@router.get("/", include_in_schema=False)
def admin_root():
    return RedirectResponse(url="/admin/login")
