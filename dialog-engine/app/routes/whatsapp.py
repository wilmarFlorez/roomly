from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.services import whatsapp_service
from app.services.whatsapp_client import send_whatsapp_message

router = APIRouter()


@router.get("/webhook")
async def verify_webhook(req: Request):
    params = dict(req.query_params)

    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == settings.whatsapp_verify_token
    ):
        challenge = params.get("hub.challenge")
        return Response(
            content=str(challenge), status_code=200, media_type="text/plain"
        )

    return JSONResponse(status_code=403, content={"error": "invalid token"})


@router.post("/webhook")
async def receive_messages(req: Request):
    data = await req.json()
    print("RECEIVE MESSAGE", data)

    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]
        messages = value.get("messages", [])

        if messages:
            message = messages[0]
            from_number = message["from"]
            text = message["text"]["body"].strip().lower()
            print("TEXT", text)

            response_text = whatsapp_service.proccess_message(text, from_number)
            await send_whatsapp_message(from_number, response_text)
            print("MESSAGE SENT")

    except Exception as e:
        print("[ERROR] procesando el mensaje: ", e)

    return {"status": "ok"}
