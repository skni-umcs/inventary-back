from . import session
from core.models.userModel import UserModel


def add(item: UserModel):
    session.add(item)
    session.commit()


def get_by_id(userId: int):
    item = session.query(UserModel).filter(UserModel.id == userId).first()

    return item


def get_by_username(username: str):
    items = session.query(UserModel).filter(UserModel.username == username).first()

    return items
