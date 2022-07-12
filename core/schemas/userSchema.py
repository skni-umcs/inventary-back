from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int | None = None
    username: str
    password: str
