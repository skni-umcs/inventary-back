import core.crud.warehouseCrud as WC
from core.models.warehouseModel import WarehouseModel
from core.schemas.warehouseSchema import WarehouseSchema


def get_by_name(warehouseName: str):
    warehouseModel: WarehouseModel = WC.get_by_name(warehouseName)

    warehouseSchema = WarehouseSchema(
        id=warehouseModel.id,
        name=warehouseModel.name
    )

    return warehouseSchema


def get_by_id(warehouseId: int):
    warehouseModel: WarehouseModel = WC.get_by_id(warehouseId)

    warehouseSchema = WarehouseSchema(
        id=warehouseModel.id,
        name=warehouseModel.name
    )

    return warehouseSchema


def get_all():
    warehouseModels = WC.get_all()

    warehouseSchemes = []
    for warehouseModel in warehouseModels:
        warehouseSchema = WarehouseSchema(
            id=warehouseModel.id,
            name=warehouseModel.name
        )
        warehouseSchemes.append(warehouseSchema)

    return warehouseSchemes


def add(warehouseSchema: WarehouseSchema):

    exists = True

    try:
        get_by_name(warehouseSchema.name)
    except AttributeError:
        exists = False

    assert not exists

    warehouseModel = WarehouseModel(
        name=warehouseSchema.name
    )

    WC.add(warehouseModel)


def delete(warehouseId: int):
    get_by_id(warehouseId)
    WC.delete(warehouseId)


def edit(warehouseSchema: WarehouseSchema):
    exists = True

    try:
        get_by_name(warehouseSchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = WarehouseSchema(
        id=warehouseSchema.id,
        name=warehouseSchema.name
    )

    WC.edit(categoryModel)
