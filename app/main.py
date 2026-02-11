from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import api_router
from app.core.config import settings
from app.core.scheduler import start_scheduler

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix="/api")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
@app.on_event("startup")
def _startup():
    start_scheduler()