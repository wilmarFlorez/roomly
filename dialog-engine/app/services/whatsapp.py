# import os
# import request
# import json
# from ..core.config import settings

# def send_whatsapp_message(data):
#   url = "https://graph.facebook.com/v19.0/382988971554015/messages"
#   headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {settings.whatsapp_authorization_token}'
#   }

#   try:
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     print(response.text)
#   except requests.exceptions.RequestException as e:
#     print(f'Error whatsapp service {e}')
    
    
def proccess_message():
  print("Procesando mensaje...")
