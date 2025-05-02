from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
  db_hostname: str
  db_port: str
  db_password: str
  db_name: str
  db_username: str
  
  class config:
    env_file = ".env"
    
    
settings = Settings() # type: ignore