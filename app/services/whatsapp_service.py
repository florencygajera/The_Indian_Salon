import requests
from app.core.config import settings

class WhatsAppService:
    @staticmethod
    def send_new_booking(booking):
        if not settings.WHATSAPP_TO_PHONE:
            return

        text = (
            f"New Booking ✅\n"
            f"Name: {booking.customer_name}\n"
            f"Phone: {booking.customer_phone}\n"
            f"Time: {booking.starts_at} to {booking.ends_at}\n"
            f"Service ID: {booking.service_id}\n"
        )

        if settings.WHATSAPP_PROVIDER == "cloud":
            WhatsAppService._send_cloud(text)
        else:
            WhatsAppService._send_twilio(text)

    @staticmethod
    def _send_cloud(text: str):
        # Meta WhatsApp Cloud API
        if not (settings.WHATSAPP_CLOUD_TOKEN and settings.WHATSAPP_CLOUD_PHONE_ID):
            return

        url = f"https://graph.facebook.com/v19.0/{settings.WHATSAPP_CLOUD_PHONE_ID}/messages"
        headers = {"Authorization": f"Bearer {settings.WHATSAPP_CLOUD_TOKEN}"}
        payload = {
            "messaging_product": "whatsapp",
            "to": settings.WHATSAPP_TO_PHONE,
            "type": "text",
            "text": {"body": text},
        }
        requests.post(url, json=payload, headers=headers, timeout=15)

    @staticmethod
    def _send_twilio(text: str):
        # If you use Twilio later, implement with twilio-python or REST
        return
