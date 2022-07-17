import core.crud.warehouseCrud as WC
from core.models.warehouseModel import WarehouseModel
from core.schemas.warehouseSchema import WarehouseSchema
from . import Session


def get_by_name(session: Session, warehouseName: str):
    warehouseModel: WarehouseModel = WC.get_by_name(session, warehouseName)

    warehouseSchema = WarehouseSchema(
        id=warehouseModel.id,
        name=warehouseModel.name
    )

    return warehouseSchema


def get_by_id(session: Session, warehouseId: int):
    warehouseModel: WarehouseModel = WC.get_by_id(session, warehouseId)

    warehouseSchema = WarehouseSchema(
        id=warehouseModel.id,
        name=warehouseModel.name
    )

    return warehouseSchema


def get_all(session: Session):
    warehouseModels = WC.get_all(session)

    warehouseSchemes = []
    for warehouseModel in warehouseModels:
        warehouseSchema = WarehouseSchema(
            id=warehouseModel.id,
            name=warehouseModel.name
        )
        warehouseSchemes.append(warehouseSchema)

    return warehouseSchemes


def add(session: Session, warehouseSchema: WarehouseSchema):

    exists = True

    try:
        get_by_name(session, warehouseSchema.name)
    except AttributeError:
        exists = False

    assert not exists

    warehouseModel = WarehouseModel(
        name=warehouseSchema.name
    )

    WC.add(session, warehouseModel)


def delete(session: Session, warehouseId: int):
    get_by_id(session, warehouseId)
    WC.delete(session, warehouseId)


def edit(session: Session, warehouseSchema: WarehouseSchema):
    exists = True

    try:
        get_by_name(session, warehouseSchema.name)
    except AttributeError:
        exists = False

    assert not exists

    categoryModel = WarehouseModel(
        id=warehouseSchema.id,
        name=warehouseSchema.name
    )

    WC.edit(session, categoryModel)
