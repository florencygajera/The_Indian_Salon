from fastapi import APIRouter
from app.api.routes import public, auth, bookings, admin, services

from app.api.routes import public, auth, bookings, admin, services, instagram


api_router = APIRouter()
api_router.include_router(public.router)
api_router.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
api_router.include_router(services.router, prefix="/api/services", tags=["Services"])
api_router.include_router(bookings.router, prefix="/api/bookings", tags=["Bookings"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
api_router.include_router(instagram.router, prefix="/api/instagram", tags=["Instagram"])
