from sqlalchemy.orm import Session
from . import models, schemas


async def create_timestamp(db: Session, timestamp: schemas.TimeStamp):
    db_timestamp = models.TimeStamp(**timestamp.dict())
    db.add(db_timestamp)
    db.commit()
    db.refresh(db_timestamp)
    return db_timestamp


async def create_dog(db: Session, dog: schemas.Dog):
    db_dog = models.Dog(**dog.dict())
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog


async def get_dogs(db: Session, kind: str | None):
    if kind is None:
        return db.query(models.Dog).all()
    return db.query(models.Dog).filter(models.Dog.kind == kind).all()


async def get_dog(db: Session, dog_pk: int):
    return db.query(models.Dog).filter(models.Dog.pk == dog_pk).first()


async def update_dog(db: Session, dog: schemas.Dog, dog_pk: int):
    db_dog = db.query(models.Dog).filter(models.Dog.pk == dog_pk).one_or_none()

    if db_dog is None:
        return None

    for var, value in vars(dog).items():
        setattr(db_dog, var, value) if value else None
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return dog
