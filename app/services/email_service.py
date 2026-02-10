import smtplib
from email.mime.text import MIMEText
from app.core.config import settings

class EmailService:
    @staticmethod
    def send_new_booking(booking):
        if not (settings.SMTP_USER and settings.SMTP_PASS and settings.ADMIN_EMAIL):
            return  # silently skip if not configured

        body = (
            f"New Booking Received!\n\n"
            f"Name: {booking.customer_name}\n"
            f"Phone: {booking.customer_phone}\n"
            f"Starts: {booking.starts_at}\n"
            f"Ends: {booking.ends_at}\n"
            f"Service ID: {booking.service_id}\n"
            f"Staff ID: {booking.staff_id}\n"
        )
        msg = MIMEText(body)
        msg["Subject"] = "New Salon Booking"
        msg["From"] = settings.SMTP_FROM or settings.SMTP_USER
        msg["To"] = settings.ADMIN_EMAIL

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as s:
            s.starttls()
            s.login(settings.SMTP_USER, settings.SMTP_PASS)
            s.send_message(msg)
