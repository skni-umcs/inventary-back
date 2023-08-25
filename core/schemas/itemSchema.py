from pydantic import BaseModel
from datetime import date


class ItemSchema(BaseModel):
    id: int | None = None
    name: str
    category: str
    value: str
    warehouse: str
    description: str
    keywords: list

    user_id: int | None = None

    added_date: date | None = None
    deleted_date: str | None = None
