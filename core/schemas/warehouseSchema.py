from pydantic import BaseModel


class WarehouseSchema(BaseModel):
    id: int | None = None
    name: str
