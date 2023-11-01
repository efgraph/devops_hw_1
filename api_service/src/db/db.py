import sqlalchemy
from core.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(settings.db_url)
metadata = sqlalchemy.MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
