import time
from enum import Enum

from pydantic import BaseModel


class DogType(str, Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'


class Dog(BaseModel):
    pk: int
    name: str
    kind: DogType

    class Config:
        orm_mode = True
        use_enum_values = True


class TimeStamp(BaseModel):
    id: int | None = None
    timestamp: int = int(time.time())

    class Config:
        orm_mode = True
