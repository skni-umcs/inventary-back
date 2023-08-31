import core.crud.itemCrud as IC
import core.db.categoryDb as CD
import core.db.warehouseDb as WD
from core.models.itemModel import ItemModel
from core.models.categoryModel import CategoryModel
from core.models.warehouseModel import WarehouseModel
from core.schemas.itemSchema import ItemSchema
from . import Session, datetime


def add(session: Session, itemSchema: ItemSchema, userId: int):

    categoryModel: CategoryModel = CD.get_by_name(session, itemSchema.category)
    categoryId = categoryModel.id

    warehouseModel: WarehouseModel = WD.get_by_name(session, itemSchema.warehouse)
    warehouseId = warehouseModel.id

    try:
        value = float(itemSchema.value)
    except ValueError:
        value = None

    keyword_string = ";".join(itemSchema.keywords)
    itemModel = ItemModel(
        name=itemSchema.name,
        category_id=categoryId,
        value=value,
        warehouse_id=warehouseId,
        description=itemSchema.description,
        keywords=keyword_string,
        user_id=userId,
        added_date=datetime.utcnow()
    )
    IC.add(session, itemModel)


def get_by_id(session: Session, itemId: int):
    model = IC.get_by_id(session, itemId)
    categoryModel = CD.get_by_id(session, model.category_id)
    warehouseModel = WD.get_by_id(session, model.warehouse_id)
    keywords = model.keywords.split(';')
    value = str(model.value)

    itemSchema = ItemSchema(
        id=model.id,
        name=model.name,
        category=categoryModel.name,
        value=value,
        warehouse=warehouseModel.name,
        description=model.description,
        keywords=keywords,
        user_id=model.user_id
    )

    return itemSchema


def get_list(session: Session, length: int = 10, skip: int = 0):

    models = IC.get_list(session, length=length, skip=skip)

    itemSchemas = []
    for model in models:
        categorySchema = CD.get_by_id(session, model.category_id)
        warehouseSchema = WD.get_by_id(session, model.warehouse_id)
        keywords = model.keywords.split(';')
        value = str(model.value)
        itemSchema = ItemSchema(
            id=model.id,
            name=model.name,
            category=categorySchema.name,
            value=value,
            warehouse=warehouseSchema.name,
            description=model.description,
            keywords=keywords,
            user_id=model.user_id
        )
        itemSchemas.append(itemSchema)

    return itemSchemas


def delete(session: Session, itemId: int):
    get_by_id(session, itemId)
    IC.delete(session, itemId)


def edit(session: Session, itemSchema: ItemSchema):

    categoryModel: CategoryModel = CD.get_by_name(session, itemSchema.category)
    categoryId = categoryModel.id

    warehouseModel: WarehouseModel = WD.get_by_name(session, itemSchema.warehouse)
    warehouseId = warehouseModel.id

    try:
        value = float(itemSchema.value)
    except ValueError:
        value = None

    keyword_string = ";".join(itemSchema.keywords)

    itemModel = ItemModel(
        id=itemSchema.id,
        name=itemSchema.name,
        category_id=categoryId,
        value=value,
        warehouse_id=warehouseId,
        description=itemSchema.description,
        keywords=keyword_string,
        user_id=itemSchema.user_id
    )

    IC.edit(session, itemModel)
