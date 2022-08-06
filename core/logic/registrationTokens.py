import string
import random

from . import Session
import core.db.registrationTokenDb as RTD
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
