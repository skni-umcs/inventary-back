from . import session
from core.schemas.itemSchema import ItemSchema as ItemSchema
from core.models.itemModel import ItemModel as ItemModel


def add(item: ItemSchema):
    category_id = 1  # TODO find category id
    try:
        value = float(item.value)
    except ValueError:
        value = None
    warehouse_id = 1  # TODO find warehouse id
    user_id = 3  # TODO determine user id
    keyword_string = " ".join(item.keywords)
    row = ItemModel(item.name, category_id, value, warehouse_id, item.description, keyword_string, user_id)
    session.add(row)
    session.commit()


def get_by_id(itemId: int):
    item = session.query(ItemModel).filter(ItemModel.id == itemId).first()

    return item
