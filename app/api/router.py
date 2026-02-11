from fastapi import APIRouter
from app.api.routes.services import router as services_router
from app.api.routes.bookings import router as bookings_router
from app.api.routes.auth import router as auth_router

api_router = APIRouter()
api_router.include_router(services_router, prefix="/services", tags=["services"])
api_router.include_router(bookings_router, prefix="/bookings", tags=["bookings"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
