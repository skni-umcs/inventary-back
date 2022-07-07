from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.schemas.itemSchema import ItemSchema
import core.crud.itemCrud as IC

router = APIRouter()


@router.post("/add")
def add(item: ItemSchema, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    IC.add(item)

    return {
        "message": "success",
    }
