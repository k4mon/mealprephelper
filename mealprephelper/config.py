from environs import Env
from fastapi.security import OAuth2PasswordBearer

env = Env()

SECRET_KEY = env("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
origins = [env("ACCEPTED_ORIGIN")]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
