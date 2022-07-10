from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str

    def __init__(self, id: int, name: str):
        super(CategorySchema, self).__init__()

        self.id = id
        self.name = name
