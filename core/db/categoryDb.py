import core.crud.categoryCrud as CC
from core.schemas.categorySchema import CategorySchema
from core.models.categoryModel import CategoryModel


def get_by_id(categoryId: int):
    categoryModel: CategoryModel = CC.get_by_id(categoryId)

    categorySchema = CategorySchema(
        id=categoryModel.id,
        name=categoryModel.name
    )

    return categorySchema


def get_by_name(categoryName: str):
    categoryModel: CategoryModel = CC.get_by_name(categoryName)

    categorySchema = CategorySchema(
        id=categoryModel.id,
        name=categoryModel.name
    )

    return categorySchema
