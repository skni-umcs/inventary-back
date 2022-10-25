from . import Session
from core.models.itemModel import ItemModel


def add(session: Session, itemModel: ItemModel):
    session.add(itemModel)
    session.commit()


def get_by_id(session: Session, itemId: int):
    itemModel: ItemModel = session.query(ItemModel).filter(ItemModel.id == itemId).first()

    return itemModel


def get_all_xd(session: Session):
    items = session.query(ItemModel)

    return items


def get_list(session: Session, length: int = 10, skip: int = 0):
    itemModels = session.query(ItemModel).offset(skip).limit(length)

    return itemModels


def delete(session: Session, itemId: int):
    session.query(ItemModel).filter(ItemModel.id == itemId).delete()
    session.commit()


def edit(session: Session, editModel: ItemModel):
    itemModel: ItemModel = session.query(ItemModel).filter(ItemModel.id == editModel.id).first()  # TODO change to function call

    itemModel.name = editModel.name
    itemModel.value = editModel.value
    itemModel.keywords = editModel.keywords
    itemModel.category_id = editModel.category_id
    itemModel.warehouse_id = editModel.warehouse_id
    itemModel.description = editModel.description
    itemModel.user_id = editModel.user_id

    session.commit()
