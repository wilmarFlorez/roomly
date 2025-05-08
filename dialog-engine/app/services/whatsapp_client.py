import httpx
from app.core.config import settings

WHATSAPP_API_URL = f"https://graph.facebook.com/v19.0/{settings.whatsapp_phone_number_id}/messages"

HEADERS = {
  "Authorization": f"Bearer {settings.whatsapp_access_token}",
  "Content-Type": "application/json"
}

async def send_whatsapp_message(to: str, message: str):
    print("SENDING MESSAGE")
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "text",
        "text": {"body": message},
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(WHATSAPP_API_URL, headers=HEADERS, json=payload)
        if response.status_code != 200:
            print("[ERROR] sending message: ", response.text)
