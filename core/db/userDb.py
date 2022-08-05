import core.crud.userCrud as UC
from core.models.userModel import UserModel
from core.schemas.userSchema import UserSchema
from . import Session


def get_by_username(session: Session, username: str):
    model: UserModel = UC.get_by_username(session, username)

    userSchema = UserSchema(
        id=model.id,
        username=model.username,
        password=model.hashed_password
    )

    return userSchema


def get_username_by_id(session: Session, userId: int) -> str:
    userModel: UserModel = UC.get_by_id(session, userId)

    username = userModel.username

    return username
