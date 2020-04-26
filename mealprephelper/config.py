from environs import Env

env = Env()

SECRET_KEY = env("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
origins = ["http://localhost:3000"]
