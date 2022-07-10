from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.routes.endpoints.itemEndpoints import list_, add
import core.db.itemDb as ID

router = APIRouter()

router.include_router(list_.router)
router.include_router(add.router)


@router.get("/")
def get_item(itemId: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    return ID.get_by_id(itemId)
