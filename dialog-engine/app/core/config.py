from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

# environments dev, stg, prod
ENV = os.getenv("ENVIRONMENT", "dev")

if ENV != "prod":
    env_path = Path(f".env.{ENV}")
    load_dotenv(dotenv_path=Path(env_path))
    print(f"[INFO] Loaded env file: {env_path}")


class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str
    whatsapp_verify_token: str
    environment: str = ENV
    whatsapp_access_token: str
    whatsapp_phone_number_id: str


settings = Settings()  # type: ignore
