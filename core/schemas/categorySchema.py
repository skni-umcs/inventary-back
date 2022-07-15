from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int | None = None
    name: str
