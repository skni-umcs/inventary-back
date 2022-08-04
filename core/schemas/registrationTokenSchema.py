from pydantic import BaseModel


class RegistrationTokenSchema(BaseModel):
    id: int
    token: str
    users_limit: int
    users_registered: int
    creator_username: str
