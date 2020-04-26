from datetime import datetime, timedelta

import jwt

from mealprephelper.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_username_from_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)["sub"]
