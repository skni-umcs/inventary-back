import core.crud.userCrud as UC
from core.schemas.userSchema import UserSchema


def get_by_username(username: str):
    model = UC.get_by_username(username)

    user = UserSchema(
        username=model.username,
        password=model.hashed_password
    )

    return user
