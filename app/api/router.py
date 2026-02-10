from fastapi import APIRouter

from app.api.routes.public import router as public_router
from app.api.routes.auth import router as auth_router
from app.api.routes.bookings import router as bookings_router
from app.api.routes.admin import router as admin_router
from app.api.routes.services import router as services_router

api_router = APIRouter()

api_router.include_router(public_router)
api_router.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
api_router.include_router(services_router, prefix="/api/services", tags=["Services"])
api_router.include_router(bookings_router, prefix="/api/bookings", tags=["Bookings"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
