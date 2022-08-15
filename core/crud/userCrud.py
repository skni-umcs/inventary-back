from . import Session
from core.models.userModel import UserModel


def add(session: Session, userModel: UserModel):
    session.add(userModel)
    session.commit()


def get_by_id(session: Session, userId: int):
    userModel = session.query(UserModel).filter(UserModel.id == userId).first()

    return userModel


def get_by_username(session: Session, username: str):
    userModel = session.query(UserModel).filter(UserModel.username == username).first()

    return userModel
