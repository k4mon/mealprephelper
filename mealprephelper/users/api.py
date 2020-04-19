from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from mealprephelper.database.database import get_db
from mealprephelper.users import schemas as user_schema, service as user_service

router = APIRouter()


@router.post("/users/", response_model=user_schema.User)
def create_user(
    user: user_schema.UserCreate, db: Session = Depends(get_db),
):
    return user_service.create_user(db, user)


@router.post("/token", response_model=user_schema.Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    if user := user_service.authenticate_user(
        db, form_data.username, form_data.password
    ):
        return {
            "access_token": user_service.create_access_token(data={"sub": user.email}),
            "token_type": "bearer",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
