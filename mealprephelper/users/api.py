from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from mealprephelper.users.factory import create_user_service
from mealprephelper.users.service.interface import AbstractUserService, UnauthorizedError
from mealprephelper.users.service.schema import User, UserCreate, Token

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(
    user: UserCreate, user_service: AbstractUserService = Depends(create_user_service)
):
    return user_service.create_user(user)


@router.post("/token", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: AbstractUserService = Depends(create_user_service),
):
    try:
        return user_service.authenticate_user(form_data.username, form_data.password)
    except UnauthorizedError:
        raise HTTPException(status_code=403)
