from datetime import timedelta, datetime

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from mealprephelper.config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from mealprephelper.users import schemas, models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _hash_password(password):
    return pwd_context.hash(password)


def _verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = _hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


def authenticate_user(db: Session, user_email: str, password: str):
    user = get_user(db, user_email)
    if not user:
        return False
    if not _verify_password(password, user.hashed_password):
        return False
    return user


def get_user(db: Session, user_email: str):
    user = db.query(models.User).filter(models.User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


def create_access_token(*, data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
