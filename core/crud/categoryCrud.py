from . import session
from core.models.categoryModel import CategoryModel


def get_by_id(categoryId: int):
    model = session.query(CategoryModel).filter(CategoryModel.id == categoryId).first()

    return model

