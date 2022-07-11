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

