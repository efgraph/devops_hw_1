import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from db.db import metadata

Base = declarative_base()

dogs = sqlalchemy.Table(
    "dogs",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("kind", sqlalchemy.String),
)

timestamps = sqlalchemy.Table(
    "timestamps",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, default=None),
    sqlalchemy.Column("timestamp", sqlalchemy.Integer)
)


class Dog(Base):
    __tablename__ = "dogs"

    pk = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kind = Column(String)


class TimeStamp(Base):
    __tablename__ = "timestamps"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
