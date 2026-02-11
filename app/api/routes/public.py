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
    return templates.TemplateResponse("home.html", {"request": request, "salon": SALON, "active": "home"})


@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "salon": SALON})

@router.get("/services", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse(
        "services.html",
        {"request": request, "salon": SALON, "active": "services"}
    )

@router.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request, "salon": SALON})

@router.get("/booking", response_class=HTMLResponse)
def booking(request: Request):
    return templates.TemplateResponse("booking.html", {"request": request, "salon": SALON, "active": "booking"})
0

@router.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "salon": SALON})

@router.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request, db: Session = Depends(get_db)):
    posts = InstagramService.get_gallery(db)
    return templates.TemplateResponse("gallery.html", {"request": request, "salon": SALON, "posts": posts})

@router.get("/skin_service", response_class=HTMLResponse)
def skin_service(request: Request):
    page = {
        "kicker": "Skin Care",
        "title": "Skin Services",
        "subtitle": "Professional facials, cleanups & glow treatments in Nikol.",
        "includes": [
            {"title": "Face Cleanup", "desc": "Deep cleansing & tan removal."},
            {"title": "Facial Treatment", "desc": "Hydrating & glow boosting facials."},
            {"title": "D-Tan", "desc": "Instant brightness treatment."},
            {"title": "Head Massage", "desc": "Relaxing add-on therapy."},
        ],
        "packages": [
            {"name": "Basic Glow", "desc": "Cleanup + Detan", "price": "499+"},
            {"name": "Signature Facial", "desc": "Facial + Massage", "price": "999+"},
            {"name": "Premium Treatment", "desc": "Advanced Glow Therapy", "price": "1499+"},
        ],
    }
    return templates.TemplateResponse(
        "services.html",
        {"request": request, "salon": SALON, "page": page}
    )


@router.get("/hair-treatment", response_class=HTMLResponse)
def hair_treatment(request: Request):
    page = {
        "kicker": "Hair Care",
        "title": "Hair Treatments",
        "subtitle": "Haircut, styling, color & spa services.",
        "includes": [
            {"title": "Haircut & Styling", "desc": "Trendy and event looks."},
            {"title": "Hair Color", "desc": "Highlights & full color."},
            {"title": "Hair Spa", "desc": "Deep nourishment therapy."},
            {"title": "Smoothening", "desc": "Long-lasting sleek finish."},
        ],
        "packages": [
            {"name": "Haircut + Wash", "desc": "Clean finish styling", "price": "299+"},
            {"name": "Hair Spa", "desc": "Repair & Shine treatment", "price": "799+"},
            {"name": "Color Package", "desc": "Color + Care", "price": "1499+"},
        ],
    }
    return templates.TemplateResponse(
        "services.html",
        {"request": request, "salon": SALON, "page": page}
    )


@router.get("/bridal-makeup", response_class=HTMLResponse)
def bridal_makeup(request: Request):
    page = {
        "kicker": "Makeup",
        "title": "Bridal Makeup",
        "subtitle": "Premium bridal & occasion makeup packages.",
        "includes": [
            {"title": "Bridal Makeup", "desc": "Long-lasting luxury finish."},
            {"title": "Hairstyling", "desc": "Bridal hairstyle support."},
            {"title": "Draping", "desc": "Saree / Dupatta draping."},
            {"title": "Touch-up Kit", "desc": "Basic touch-up support."},
        ],
        "packages": [
            {"name": "Engagement Look", "desc": "Soft glam finish", "price": "2999+"},
            {"name": "Bridal Premium", "desc": "Full bridal package", "price": "6999+"},
            {"name": "Bridal Combo", "desc": "Makeup + Hair + Draping", "price": "9999+"},
        ],
    }
    return templates.TemplateResponse(
        "services.html",
        {"request": request, "salon": SALON, "page": page}
    )
