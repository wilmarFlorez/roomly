from fastapi import status, Depends, APIRouter, HTTPException
from .. import schemas
from ..models import models
from sqlalchemy.orm import Session
from ..database import get_db
from app.services import user_service

router = APIRouter(prefix="/users")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name,
        phone_number=user.phone_number,
        phone_number_id=user.phone_number_id,
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{phone_id}", response_model=schemas.UserResponse)
def get_user_by_phone_id(phone_id: str, db: Session = Depends(get_db)):
    return user_service.get_user_by_phone_id(phone_id, db)
