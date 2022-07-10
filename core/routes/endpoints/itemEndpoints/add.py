from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.schemas.itemSchema import ItemSchema
import core.db.itemDb as ID

router = APIRouter()


@router.post("/add")
def add(item: ItemSchema, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    ID.add(item)

    return {
        "message": "success",
    }
