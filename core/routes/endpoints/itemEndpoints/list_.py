from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.itemDb as ID

router = APIRouter()


@router.get("/list")
def get_list_of_items(length: int, skip: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    items = ID.get_list(length, skip)

    return items
