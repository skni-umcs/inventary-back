from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.schemas.itemSchema import ItemSchema
import core.crud.itemCrud as ic

router = APIRouter()


@router.get("/list")
def list_(length: int, skip: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    itemik = ItemSchema(id=2, name="item123", category="Potężna kategoria szachowa", value="W ciul ", warehouse="koło",
                        description="Potężny opisik", keywords=['Jeżyk'])
    return [
        itemik
    ]
