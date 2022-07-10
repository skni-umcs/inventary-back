import core.crud.categoryCrud as CC
from core.schemas.categorySchema import CategorySchema


def get_by_id(categoryId: int):
    model = CC.get_by_id(categoryId)
