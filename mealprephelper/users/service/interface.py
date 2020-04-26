import abc

from mealprephelper.users.schema import UserCreate, User, Token


class UnauthorizedError(Exception):
    pass


class AbstractUserService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_user(self, user: UserCreate) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def authenticate_user(self, email: str, password: str) -> Token:
        raise NotImplementedError
