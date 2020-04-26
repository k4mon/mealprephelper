from mealprephelper.users.service.interface import AbstractUserService
from mealprephelper.users.service.service import UserService
from mealprephelper.users.storage.storage import InMemoryUserStorage

storage = InMemoryUserStorage()


def create_user_service() -> AbstractUserService:
    return UserService(storage=storage)
