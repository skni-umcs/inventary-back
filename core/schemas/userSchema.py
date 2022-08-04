from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int | None = None
    username: str
    password: str
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    privileges_id: int | None = None
