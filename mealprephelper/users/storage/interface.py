import abc

from mealprephelper.users.schema import UserWithHashedPassword, User


class AbstractUserStorage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, user: UserWithHashedPassword) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_hashed_password(self, username: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def exists(self, username: str) -> bool:
        raise NotImplementedError
