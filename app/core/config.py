from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "THE INDIAN SALON - Nikol"
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/indian_salon"

    JWT_SECRET: str = "CHANGE_ME_SUPER_SECRET"
    JWT_ALGO: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASS: str = ""
    SMTP_FROM: str = ""
    ADMIN_EMAIL: str = ""

    # WhatsApp (choose one approach)
    WHATSAPP_PROVIDER: str = "cloud"  # "cloud" or "twilio"
    WHATSAPP_CLOUD_TOKEN: str = ""
    WHATSAPP_CLOUD_PHONE_ID: str = ""
    WHATSAPP_TO_PHONE: str = ""      # salon owner phone in WhatsApp format like 91xxxxxxxxxx

    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_WHATSAPP_FROM: str = "whatsapp:+14155238886"

    IG_USER_ID: str = ""
    IG_ACCESS_TOKEN: str = ""
    IG_SYNC_LIMIT: int = 12


    class Config:
        env_file = ".env"

settings = Settings()
