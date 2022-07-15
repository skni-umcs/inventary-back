from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    name: str
    category: str
    value: str
    warehouse: str
    description: str
    keywords: list
    user_id: int
