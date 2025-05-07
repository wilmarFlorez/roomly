from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas
from ..models import models
from sqlalchemy.orm import Session
from ..database import get_db

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
def get_user(phone_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.phone_number_id == phone_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {phone_id} does not exist",
        )
    return user
