from . import session
from core.models.itemModel import ItemModel


def add(item: ItemModel):
    session.add(item)
    session.commit()


def get_by_id(itemId: int):
    item = session.query(ItemModel).filter(ItemModel.id == itemId).first()

    return item


def get_all_xd():
    items = session.query(ItemModel)

    return items


def get_list(length: int = 10, skip: int = 0):
    items = session.query(ItemModel).offset(skip).limit(length)

    return items
