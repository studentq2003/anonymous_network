from uuid import UUID

from sqlalchemy.orm import Session

from app.core import models
from app.core import schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_item(db: Session, uuid: str):
    return db.query(models.Post).filter(models.Post.uuid == uuid).first()


def create_user_item(db: Session, item: schemas.PostCreate, uuid: UUID):
    db_item = models.Post(uuid=uuid, title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
