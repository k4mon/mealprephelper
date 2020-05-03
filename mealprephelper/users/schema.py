from pydantic.main import BaseModel


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserWithHashedPassword(UserBase):
    hashed_password: str


class User(UserBase):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
