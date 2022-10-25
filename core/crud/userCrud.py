from . import Session, func
from core.models.userModel import UserModel


def add(session: Session, userModel: UserModel) -> None:
    session.add(userModel)
    session.commit()


def get_by_id(session: Session, userId: int) -> UserModel:
    userModel = session.query(UserModel).filter(UserModel.id == userId).first()

    return userModel


def get_by_lowercase_username(session: Session, username: str) -> UserModel:
    userModel = session.query(UserModel).filter(func.lower(UserModel.username) == username.lower()).first()

    return userModel


def get_by_email(session: Session, email: str) -> UserModel:
    userModel = session.query(UserModel).filter(UserModel.email == email).first()

    return userModel
