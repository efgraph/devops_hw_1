import asyncio

from sqlalchemy.orm import Session

from . import crud
from .schemas import Dog, TimeStamp

dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}


async def init_timestamps(db: Session):
    async def create_timestamp():
        await crud.create_timestamp(db, timestamp=TimeStamp())

    timestamps = await crud.get_timestamps(db)
    if not timestamps or len(timestamps) == 0:
        coros = [create_timestamp() for _ in range(2)]
        await asyncio.gather(*coros)


async def init_dogs(db: Session):
    async def create_dog(dog: Dog):
        await crud.create_dog(db, dog=dog)

    dogs = await crud.get_dogs(db, None)
    if not dogs or len(dogs) == 0:
        coros = [create_dog(dog) for dog in dogs_db.values()]
        await asyncio.gather(*coros)


async def init_db(db: Session) -> None:
    await init_timestamps(db)
    await init_dogs(db)
