from . import session
from core.models.categoryModel import CategoryModel


def get_by_id(categoryId: int):
    categoryModel = session.query(CategoryModel).filter(CategoryModel.id == categoryId).first()

    return categoryModel


def get_by_name(categoryName: str):
    categoryModel = session.query(CategoryModel).filter(CategoryModel.name == categoryName).first()

    return categoryModel


def get_all():
    categoryModels = session.query(CategoryModel)

    return categoryModels


def add(categoryModel: CategoryModel):
    session.add(categoryModel)
    session.commit()


def delete(categoryId: int):
    session.query(CategoryModel).filter(CategoryModel.id == categoryId).delete()
    session.commit()


def edit(editModel: CategoryModel):
    categoryModel: CategoryModel = session.query(CategoryModel).filter(CategoryModel.id == editModel.id).first()

    categoryModel.name = editModel.name

    session.commit()
