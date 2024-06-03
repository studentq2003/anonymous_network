import datetime

import uuid
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
