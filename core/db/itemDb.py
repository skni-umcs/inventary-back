import core.crud.itemCrud as IC
import core.crud.categoryCrud as CC
import core.crud.warehouseCrud as WC
from core.models.itemModel import ItemModel
from core.schemas.itemSchema import ItemSchema


def add(item: ItemSchema):
    category_id = 1  # TODO find category id
    try:
        value = float(item.value)
    except ValueError:
        value = None
    warehouse_id = 1  # TODO find warehouse id
    user_id = 1  # TODO determine user id
    keyword_string = ";".join(item.keywords)
    model = ItemModel(item.name, category_id, value, warehouse_id, item.description, keyword_string, user_id)
    IC.add(model)


def get_by_id(itemId: int):
    model = IC.get_by_id(itemId)

    item = ItemSchema(
        id=model.id,
        name=model.name,
        category=model.category_id,

    )


def get_list(length: int = 10, skip: int = 0):

    models = IC.get_list(length=length, skip=skip)

    items = []
    for model in models:
        categoryModel = CC.get_by_id(model.category_id)
        warehouseModel = WC.get_by_id(model.warehouse_id)
        keywords = model.keywords.split(';')
        value = str(model.value)
        item = ItemSchema(
            id=model.id,
            name=model.name,
            category=categoryModel.name,
            value=value,
            warehouse=warehouseModel.name,
            description=model.description,
            keywords=keywords
        )
        items.append(item)

    return items
