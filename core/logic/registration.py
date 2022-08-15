import string
import random

from . import Session

import core.db.userDb as UD
import core.db.registrationTokenDb as RTD

from core.schemas.userSchema import UserSchema
from core.schemas.registrationTokenSchema import RegistrationTokenSchema


def generate_token(session: Session, name: str, usersLimit: int, username: str) -> str:
    token = ''.join(random.choices(string.ascii_uppercase, k=30))

    tokenSchema = RegistrationTokenSchema(
        name=name,
        token=token,
        users_limit=usersLimit,
        users_registered=[],
        creator_username=username
    )

    RTD.add(session, tokenSchema)

    return token


def get_valid_token(session: Session, token: str) -> RegistrationTokenSchema | None:
    tokenSchema: RegistrationTokenSchema = RTD.get_by_token(session, token)

    assert tokenSchema

    if tokenSchema.users_limit <= len(tokenSchema.users_registered):
        return None

    return tokenSchema


def validate_user(session: Session, user: UserSchema) -> bool:
    assert not UD.get_by_username(session, user.username)

    assert user.password == user.password_repeat





def registerUser(session: Session, token: RegistrationTokenSchema, user: UserSchema) -> None:
    pass
