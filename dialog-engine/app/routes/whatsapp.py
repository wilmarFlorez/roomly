from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.services.whatsapp import proccess_message

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(req: Request):
  params = dict(req.query_params)
  if (params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == settings.whatsapp_verify_token):
    return JSONResponse(content=params.get("hub.challenge"))
  
  return JSONResponse(status_code=403, content={"error": "invalid token"})

@router.post("/webhook")
async def receive_messages(req: Request):
  data = await req.json()
  print('Data from whatsapp', data)
  return {"status": "ok"}