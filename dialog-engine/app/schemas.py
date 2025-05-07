from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: Optional[str] = None
    phone_number: str
    phone_number_id: str
    email: Optional[str] = None


class UserResponse(BaseModel):
    phone_number_id: str

    class config:
        orm_mode = True
