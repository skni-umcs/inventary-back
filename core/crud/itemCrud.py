from . import session
from core.models.itemModel import ItemModel


def add(itemModel: ItemModel):
    session.add(itemModel)
    session.commit()


def get_by_id(itemId: int):
    itemModel: ItemModel = session.query(ItemModel).filter(ItemModel.id == itemId).first()

    return itemModel


def get_all_xd():
    items = session.query(ItemModel)

    return items


def get_list(length: int = 10, skip: int = 0):
    itemModels = session.query(ItemModel).offset(skip).limit(length)

    return itemModels


def delete(itemId: int):
    session.query(ItemModel).filter(ItemModel.id == itemId).delete()
    session.commit()


def edit(editModel: ItemModel):
    itemModel: ItemModel = session.query(ItemModel).filter(ItemModel.id == editModel.id).first()

    itemModel.name = editModel.name
    itemModel.value = editModel.value
    itemModel.keywords = editModel.keywords
    itemModel.category_id = editModel.category_id
    itemModel.warehouse_id = editModel.warehouse_id
    itemModel.description = editModel.description
    itemModel.user_id = editModel.user_id

    session.commit()
