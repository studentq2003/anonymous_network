import datetime

import uuid

from pydantic import EmailStr
from sqlalchemy import Column, Integer, String, Date, Time

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    title = Column(String, index=True)
    description = Column(String)
    date = Column(Date, default=datetime.datetime.now().date())
    time = Column(Time, default=datetime.datetime.now().time())
    private = Column(String)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
