from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    category: str
    value: str
    warehouse: str
    description: str
    keywords: list
