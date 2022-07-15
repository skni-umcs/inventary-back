from . import session
from core.models.warehouseModel import WarehouseModel


def add(item: WarehouseModel):
    session.add(item)
    session.commit()


def get_by_id(warehouseId: int):
    item = session.query(WarehouseModel).filter(WarehouseModel.id == warehouseId).first()

    return item


def get_by_name(name: str):
    item = session.query(WarehouseModel).filter(WarehouseModel.name == name).first()

    return item
