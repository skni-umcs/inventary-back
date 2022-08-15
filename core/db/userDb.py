import core.crud.userCrud as UC
from core.models.userModel import UserModel
from core.schemas.userSchema import UserSchema
from . import Session


def get_by_username(session: Session, username: str):
    userModel: UserModel = UC.get_by_username(session, username)

    userSchema = UserSchema(
        id=userModel.id,
        username=userModel.username,
        password=userModel.hashed_password
    )

    return userSchema


def get_username_by_id(session: Session, userId: int) -> str:
    userModel: UserModel = UC.get_by_id(session, userId)

    username = userModel.username

    return username


def get_by_email(session: Session, email: str):
    userModel: UserModel = UC.get_by_email(session, email)

    userSchema = UserSchema(
        id=userModel.id,
        username=userModel.username,
        password=userModel.hashed_password
    )

    return userSchema


def add(session: Session, userSchema: UserSchema):
    userModel = UserModel(
        username=userSchema.username,
        firstname=userSchema.username,
        lastname=userSchema.lastname,
        email=userSchema.email,
        hashed_password=userSchema.password,
        privileges_id=1
    )
    UC.add(session, userModel)
