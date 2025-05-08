from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import models
from ..database import get_db
from app import schemas


async def create_user(user: schemas.UserCreate, db: Session):
    new_user = models.User(
        name=user.name,
        phone_number=user.phone_number,
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_phone_number(phone_number: str, db: Session):
    user = (
        db.query(models.User).filter(models.User.phone_number == phone_number).first()
    )
    return user
