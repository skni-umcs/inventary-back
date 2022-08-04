from core.models.categoryModel import CategoryModel
from . import Session


def get_by_id(session: Session, categoryId: int):
    categoryModel = session.query(CategoryModel).filter(CategoryModel.id == categoryId).first()

    return categoryModel


def get_by_name(session: Session, categoryName: str):
    categoryModel = session.query(CategoryModel).filter(CategoryModel.name == categoryName).first()

    return categoryModel


def get_all(session: Session):
    categoryModels = session.query(CategoryModel)

    return categoryModels


def add(session: Session, categoryModel: CategoryModel):
    session.add(categoryModel)
    session.commit()


def delete(session: Session, categoryId: int):
    session.query(CategoryModel).filter(CategoryModel.id == categoryId).delete()
    session.commit()


def edit(session: Session, editModel: CategoryModel):
    categoryModel: CategoryModel = session.query(CategoryModel).filter(CategoryModel.id == editModel.id).first()

    categoryModel.name = editModel.name

    session.commit()
