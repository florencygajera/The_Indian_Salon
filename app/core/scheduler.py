from apscheduler.schedulers.background import BackgroundScheduler
from app.db.session import SessionLocal
from app.services.instagram_service import InstagramService

scheduler = BackgroundScheduler()

def start_scheduler():
    # every 60 minutes
    scheduler.add_job(sync_job, "interval", minutes=60, id="ig_sync", replace_existing=True)
    scheduler.start()

def sync_job():
    db = SessionLocal()
    try:
        InstagramService.sync_latest(db)
    finally:
        db.close()
