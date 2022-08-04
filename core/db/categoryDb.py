import core.crud.categoryCrud as CC
from core.schemas.categorySchema import CategorySchema
from core.models.categoryModel import CategoryModel
from . import Session


def get_by_id(session: Session, categoryId: int):
    categoryModel: CategoryModel = CC.get_by_id(session, categoryId)

    categorySchema = CategorySchema(
        id=categoryModel.id,
        name=categoryModel.name
    )

    return categorySchema


def get_by_name(session: Session, categoryName: str):
    categoryModel: CategoryModel = CC.get_by_name(session, categoryName)

    categorySchema = CategorySchema(
        id=categoryModel.id,
        name=categoryModel.name
    )

    return categorySchema


def get_all(session: Session):
    categoryModels = CC.get_all(session)

    categorySchemes = []
    for categoryModel in categoryModels:
        categorySchema = CategorySchema(
            id=categoryModel.id,
            name=categoryModel.name
        )
        categorySchemes.append(categorySchema)

    return categorySchemes


def add(session: Session, categorySchema: CategorySchema):

    exists = True

    try:
        get_by_name(session, categorySchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = CategoryModel(
        name=categorySchema.name
    )

    CC.add(session, categoryModel)


def delete(session: Session, categoryId: int):
    get_by_id(session, categoryId)
    CC.delete(session, categoryId)


def edit(session: Session, categorySchema: CategorySchema):
    exists = True

    try:
        get_by_name(session, categorySchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = CategoryModel(
        id=categorySchema.id,
        name=categorySchema.name
    )

    CC.edit(session, categoryModel)
