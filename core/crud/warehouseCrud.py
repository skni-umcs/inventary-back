from . import session
from core.models.warehouseModel import WarehouseModel


def add(warehouseModel: WarehouseModel):
    session.add(warehouseModel)
    session.commit()


def get_by_id(warehouseId: int):
    warehouseModel = session.query(WarehouseModel).filter(WarehouseModel.id == warehouseId).first()

    return warehouseModel


def get_by_name(name: str):
    warehouseModel = session.query(WarehouseModel).filter(WarehouseModel.name == name).first()

    return warehouseModel


def get_all():
    warehouseModels = session.query(WarehouseModel)

    return warehouseModels


def delete(warehouseId: int):
    session.query(WarehouseModel).filter(WarehouseModel.id == warehouseId).delete()
    session.commit()


def edit(editModel: WarehouseModel):
    warehouseModel: WarehouseModel = session.query(WarehouseModel).filter(WarehouseModel.id == editModel.id).first()

    warehouseModel.name = editModel.name

    session.commit()
