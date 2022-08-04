from . import Session
from core.models.warehouseModel import WarehouseModel


def add(session: Session, warehouseModel: WarehouseModel):
    session.add(warehouseModel)
    session.commit()


def get_by_id(session: Session, warehouseId: int):
    warehouseModel = session.query(WarehouseModel).filter(WarehouseModel.id == warehouseId).first()

    return warehouseModel


def get_by_name(session: Session, name: str):
    warehouseModel = session.query(WarehouseModel).filter(WarehouseModel.name == name).first()

    return warehouseModel


def get_all(session: Session):
    warehouseModels = session.query(WarehouseModel)

    return warehouseModels


def delete(session: Session, warehouseId: int):
    session.query(WarehouseModel).filter(WarehouseModel.id == warehouseId).delete()
    session.commit()


def edit(session: Session, editModel: WarehouseModel):
    warehouseModel: WarehouseModel = session.query(WarehouseModel).filter(WarehouseModel.id == editModel.id).first()

    warehouseModel.name = editModel.name

    session.commit()
