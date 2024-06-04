from uuid import UUID

from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.core import models
from app.core import schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Post)
        .filter(models.Post.private == "public")
        .offset(skip)
        .limit(limit)
    )


def get_item(db: Session, uuid: str):
    return db.query(models.Post).filter(models.Post.uuid == uuid).first()


def get_items_by_period(db: Session, dt_from, dt_upto):
    res = []
    stmt = (
        select(models.Post)
        .filter(and_(models.Post.date >= dt_from, models.Post.date <= dt_upto))
        .filter(models.Post.private == "public")
    )
    for post in db.scalars(stmt):
        res.append(post)
    return res


def create_user_item(db: Session, item: schemas.PostCreate, uuid: UUID):
    db_item = models.Post(
        uuid=uuid, title=item.title, description=item.description, private=item.private
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
