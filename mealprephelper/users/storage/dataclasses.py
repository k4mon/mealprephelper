from dataclasses import dataclass


@dataclass
class StorageUser:
    user_id: int
    email: str
    hashed_password: str
