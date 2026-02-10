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
        "subtitle": "Facials, cleanups, detan & glow treatments for fresh, healthy skin.",
        "includes": [
            {"title": "Face Cleanup", "desc": "Deep cleanse, remove tan & impurities."},
            {"title": "Facial Treatments", "desc": "Hydration, glow and skin repair options."},
            {"title": "D-Tan & Bleach", "desc": "Brightening & even tone finishing."},
        ],
        "packages": [
            {"name": "Quick Glow", "desc": "Cleanup + mild detan", "price": "499+"},
            {"name": "Signature Facial", "desc": "Facial + massage + finishing", "price": "999+"},
            {"name": "Premium Glow", "desc": "Advanced facial + detan", "price": "1499+"},
        ],
    }
    return templates.TemplateResponse("service_detail.html", {"request": request, "salon": SALON, "active": "services", "page": page})

@router.get("/hair-treatment", response_class=HTMLResponse)
def hair_treatment(request: Request):
    page = {
        "kicker": "Hair",
        "title": "Hair Treatments",
        "subtitle": "Haircut, styling, spa, smoothening and premium hair care.",
        "includes": [
            {"title": "Haircut & Styling", "desc": "Casual & event looks."},
            {"title": "Color & Highlights", "desc": "Natural to bold transformations."},
            {"title": "Hair Spa", "desc": "Repair, smoothness and shine."},
        ],
        "packages": [
            {"name": "Haircut + Wash", "desc": "Clean finish + styling", "price": "299+"},
            {"name": "Hair Spa", "desc": "Nourish + repair treatment", "price": "799+"},
            {"name": "Color Package", "desc": "Color + care + finishing", "price": "1499+"},
        ],
    }
    return templates.TemplateResponse("service_detail.html", {"request": request, "salon": SALON, "active": "services", "page": page})

@router.get("/bridal-makeup", response_class=HTMLResponse)
def bridal_makeup(request: Request):
    page = {
        "kicker": "Makeup",
        "title": "Bridal Makeup",
        "subtitle": "Bridal and occasion looks with premium finish and photo-ready results.",
        "includes": [
            {"title": "Bridal Look", "desc": "Full makeup with long-lasting finish."},
            {"title": "Hairstyle", "desc": "Bridal hair styling as per outfit/face."},
            {"title": "Touch-up", "desc": "Final finishing for a perfect look."},
        ],
        "packages": [
            {"name": "Engagement Makeup", "desc": "Soft glam + hairstyle", "price": "2999+"},
            {"name": "Bridal Makeup", "desc": "Premium bridal look", "price": "6999+"},
            {"name": "Bridal Combo", "desc": "Makeup + hair + draping", "price": "9999+"},
        ],
    }
    return templates.TemplateResponse("service_detail.html", {"request": request, "salon": SALON, "active": "services", "page": page})
