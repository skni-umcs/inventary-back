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


def get_all():
    categoryModels = CC.get_all()

    categorySchemes = []
    for categoryModel in categoryModels:
        categorySchema = CategorySchema(
            id=categoryModel.id,
            name=categoryModel.name
        )
        categorySchemes.append(categorySchema)

    return categorySchemes


def add(categorySchema: CategorySchema):

    exists = True

    try:
        get_by_name(categorySchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = CategoryModel(
        name=categorySchema.name
    )

    CC.add(categoryModel)


def delete(categoryId: int):
    get_by_id(categoryId)
    CC.delete(categoryId)


def edit(categorySchema: CategorySchema):
    exists = True

    try:
        get_by_name(categorySchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = CategoryModel(
        id=categorySchema.id,
        name=categorySchema.name
    )

    CC.edit(categoryModel)
