from dataclasses import dataclass


@dataclass
class StorageUser:
    user_id: int
    username: str
    hashed_password: str
