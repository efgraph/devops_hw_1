import sqlalchemy.exc
from starlette.responses import Response
from starlette.status import HTTP_200_OK
from fastapi import APIRouter, HTTPException, Depends
from db.db import get_db
from db import schemas, crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/')
async def root():
    return Response(status_code=HTTP_200_OK)


@router.post('/post', response_model=schemas.TimeStamp)
async def create_timestamp(db: Session = Depends(get_db)):
    timestamp = await crud.create_timestamp(db, timestamp=schemas.TimeStamp())
    return timestamp


@router.post('/dog',
             response_model=schemas.Dog,
             description='Запись собак', )
async def create_dog(dog: schemas.Dog, db: Session = Depends(get_db)):
    try:
        dog = await crud.create_dog(db, dog)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=409, detail='The specified PK already exists')
    return dog


@router.get("/dog",
            response_model=list[schemas.Dog],
            description='Получение собак по типу, получение списка собак')
async def get_dogs(kind: schemas.DogType | None = None, db: Session = Depends(get_db)):
    dogs = await crud.get_dogs(db, kind)
    return dogs


@router.get("/dog/{pk}",
            response_model=schemas.Dog,
            description='Получение собаки по id')
async def get_dog(pk: int, db: Session = Depends(get_db)):
    dog = await crud.get_dog(db, pk)
    if dog is None:
        raise HTTPException(status_code=404, detail='Dog not found')
    return dog


@router.patch('/dog/{pk}',
              response_model=schemas.Dog,
              description='Обновление собаки по id')
async def patch_dog(pk: int, dog: schemas.Dog, db: Session = Depends(get_db)):
    if dog.pk < pk:
        raise HTTPException(status_code=409, detail='The specified PK already exists')
    try:
        dog = await crud.update_dog(db, dog, pk)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=409, detail='The specified PK already exists')
    if dog is None:
        raise HTTPException(status_code=404, detail='Dog not found')
    return dog
