from pydantic import BaseModel


class RegistrationSchema(BaseModel):
    id: int
    token_id: int
    user_id: int
