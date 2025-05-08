from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import models
from ..database import get_db



def get_user_by_phone_id(phone_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.phone_number_id == phone_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {phone_id} does not exist",
        )
    return user
