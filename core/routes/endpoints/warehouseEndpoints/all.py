from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.warehouseDb as WD

router = APIRouter()


@router.get("/all")
def get_all_warehouses(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    warehouseSchemes = WD.get_all()

    return warehouseSchemes
