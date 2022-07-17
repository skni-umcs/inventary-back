from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from core.routes.endpoints.warehouseEndpoints import all
import core.db.warehouseDb as WD
from core.schemas.warehouseSchema import WarehouseSchema
from sqlalchemy.exc import IntegrityError
from .. import get_db_session, Session

router = APIRouter()

router.include_router(all.router)


@router.get("/{warehouseAttribute}")
def get_warehouse_by_id_or_name(warehouseAttribute: int | str, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()
    if isinstance(warehouseAttribute, int):
        try:
            warehouseAttributeSchema = WD.get_by_id(session, warehouseAttribute)
        except AttributeError:
            raise HTTPException(status_code=404, detail="Warehouse with that id not found")
    else:
        try:
            warehouseAttributeSchema = WD.get_by_name(session, warehouseAttribute)
        except AttributeError:
            raise HTTPException(status_code=404, detail="Warehouse with that name not found")

    return warehouseAttributeSchema


@router.delete("/{warehouseId}")
def delete_warehouse_by_id(warehouseId: int, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        WD.delete(session, warehouseId)
    except AttributeError:
        raise HTTPException(status_code=404, detail="Category with that id not found")
    except IntegrityError:
        raise HTTPException(status_code=422, detail="Some item is assigned to that warehouse (probably :P)")

    return {
        "message": "success",
    }


@router.post("/")
def add_warehouse(warehouseSchema: WarehouseSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        WD.add(session, warehouseSchema)
    except AssertionError:
        raise HTTPException(status_code=422, detail="Warehouse with that name already exists (probably :P)")

    return {
        "message": "success",
    }


@router.put("/")
def edit_warehouse(warehouseSchema: WarehouseSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        assert warehouseSchema.id is not None
    except AssertionError:
        raise HTTPException(status_code=422, detail="Warehouse id required")

    try:
        WD.edit(warehouseSchema)
    except (AttributeError, AssertionError):
        raise HTTPException(status_code=422, detail="Warehouse with that name already exists (probably :P)")

    return {
        "message": "success",
    }
