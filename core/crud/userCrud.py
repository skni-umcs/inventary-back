from . import Session
from core.models.userModel import UserModel


def add(session: Session, item: UserModel):
    session.add(item)
    session.commit()


def get_by_id(session: Session, userId: int):
    item = session.query(UserModel).filter(UserModel.id == userId).first()

    return item


def get_by_username(session: Session, username: str):
    items = session.query(UserModel).filter(UserModel.username == username).first()

    return items
