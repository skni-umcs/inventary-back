from pydantic import BaseModel


class RegistrationTokenSchema(BaseModel):
    id: int | None = None
    name: str
    token: str
    users_limit: int
    users_registered: list[str]
    creator_username: str
