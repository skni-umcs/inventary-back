from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.warehouseDb as WD
from ... import get_db_session, Session

router = APIRouter()


@router.get("/all")
def get_all_warehouses(Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    warehouseSchemes = WD.get_all(session)

    return warehouseSchemes
