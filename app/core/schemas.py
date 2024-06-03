import uuid
from datetime import datetime
from typing import Any, Union

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: Union[str, None] = None


class PostCreate(PostBase):
    pass
    # uuid: uuid.UUID
    # date: str = datetime.now().date()
    # time: str = datetime.now().time()


class Post(PostBase):
    id: int
    uuid: str
    date: Any
    time: Any

    class Config:
        from_attributes = True
