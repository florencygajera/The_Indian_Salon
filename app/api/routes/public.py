from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import Depends
from app.api.deps import get_db
from app.services.instagram_service import InstagramService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

SALON = {
    "name": "THE INDIAN SALON",
    "phone": "+91 75758 69696",
    "address": "GF-5, 6, Palash Pearl, MG Road, Near Malabar Hills, New India Colony, Nikol, Ahmedabad, Gujarat 380049",
    "hours": "10:00 AM – 9:00 PM",
    "instagram": "https://www.instagram.com/the_indian_salon_/"
}

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "salon": SALON})

@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "salon": SALON})

@router.get("/services", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request, "salon": SALON})

@router.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request, "salon": SALON})

@router.get("/booking", response_class=HTMLResponse)
def booking(request: Request):
    return templates.TemplateResponse("booking.html", {"request": request, "salon": SALON})

@router.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "salon": SALON})

@router.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request, db: Session = Depends(get_db)):
    posts = InstagramService.get_gallery(db)
    return templates.TemplateResponse("gallery.html", {"request": request, "salon": SALON, "posts": posts})