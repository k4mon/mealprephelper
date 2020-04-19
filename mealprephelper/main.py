from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.cors import CORSMiddleware

from mealprephelper.config import origins
from mealprephelper.recipes import api as recipes_api
from mealprephelper.users import api as users_api

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_api.router, tags=["users"])

app.include_router(
    recipes_api.router, prefix="/recipes", tags=["recipes"], dependencies=[Depends(oauth2_scheme)],
)
