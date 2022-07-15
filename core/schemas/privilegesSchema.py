from pydantic import BaseModel


class PrivilegesSchema(BaseModel):
    id: int
    name: str
