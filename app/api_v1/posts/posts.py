import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core import schemas, crud
from app.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/", response_model=schemas.Post, name="create post")
def create_post(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, uuid=uuid.uuid4())


@router.post("/filter_date")
def read_posts_by_period(dt_from: str, dt_upto: str, db: Session = Depends(get_db)):
    return crud.get_items_by_period(db, dt_from, dt_upto)


@router.get("/", response_model=List[schemas.Post], name="read all posts")
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{uuid}/", response_model=schemas.Post, name="read post by uuid")
def read_post(uuid: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, uuid=uuid)
    return item
