from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.routes.endpoints.itemEndpoints import list_
import core.crud.itemCrud as IC

router = APIRouter()

router.include_router(list_.router)


@router.get("/")
def get_item(itemId: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    return IC.get_by_id(itemId)
