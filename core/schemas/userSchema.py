from pydantic import BaseModel
from typing import Union


class UserSchema(BaseModel):
    id: Union[int, None] = None
    username: str
    password: str
