import string
import random

from . import Session

import core.db.userDb as UD
import core.db.registrationDb as RD
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
    assert not UD.get_by_lowercase_username(session, user.username)
    assert user.username
    if len(user.username) < 3:
        assert None

    assert user.password
    assert user.password == user.password_repeat
    if len(user.password) < 8:
        assert None

    assert user.firstname
    assert user.lastname

    assert user.email
    assert not UD.get_by_email(session, user.email)

    return True


def registerUser(session: Session, token: RegistrationTokenSchema, userSchema: UserSchema) -> None:
    UD.add(session, userSchema)
    userId = UD.get_by_lowercase_username(session, userSchema.username).id
    token.users_registered.append(userSchema.username)
    RD.add_registration(session, token.id, userId)
