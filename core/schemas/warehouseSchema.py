from pydantic import BaseModel


class WarehouseSchema(BaseModel):
    id: int
    name: str
