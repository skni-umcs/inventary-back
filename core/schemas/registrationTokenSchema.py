from pydantic import BaseModel


class RegistrationTokenSchema(BaseModel):
    id: int
    name: str
    token: str
    users_limit: int
    users_registered: list[str]
    creator_username: str
