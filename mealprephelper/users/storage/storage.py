from mealprephelper.users.service.schema import UserWithHashedPassword, User
from mealprephelper.users.storage.dataclasses import StorageUser
from mealprephelper.users.storage.interface import AbstractUserStorage


class InMemoryUserStorage(AbstractUserStorage):
    USERS = []
    USER_ID = 0

    def _get_next_user_id(self):
        user_id = self.USER_ID
        self.USER_ID = self.USER_ID + 1
        return user_id

    def create(self, user: UserWithHashedPassword) -> User:
        new_user = StorageUser(**user.dict(), user_id=self._get_next_user_id())
        self.USERS.append(new_user)
        return User(id=new_user.user_id, email=new_user.email)

    def get_user_hashed_password(self, email: str) -> str:
        stored_user = next(user for user in self.USERS if user.email == email)
        return stored_user.hashed_password

    def exists(self, email: str):
        return any([db_user for db_user in self.USERS if db_user.email == email])
