from mealprephelper.users.service.helpers.password import hash_password, verify_password
from mealprephelper.token import create_access_token
from mealprephelper.users.service.interface import (
    AbstractUserService,
    UnauthorizedError,
    UserExistsError,
)
from mealprephelper.users.schema import UserCreate, User, UserWithHashedPassword, Token
from mealprephelper.users.storage.interface import AbstractUserStorage


class UserService(AbstractUserService):
    def __init__(self, storage: AbstractUserStorage):
        self.storage = storage

    def create_user(self, user: UserCreate) -> User:
        hashed_password = hash_password(user.password)
        if self.storage.exists(user.username):
            raise UserExistsError("User already exists")
        return self.storage.create(
            UserWithHashedPassword(username=user.username, hashed_password=hashed_password)
        )

    def authenticate_user(self, username: str, password: str) -> Token:
        user = self.storage.exists(username)
        if not user or not verify_password(
            password, self.storage.get_user_hashed_password(username)
        ):
            raise UnauthorizedError
        else:
            return Token(
                access_token=create_access_token(data={"sub": username}), token_type="bearer",
            )
