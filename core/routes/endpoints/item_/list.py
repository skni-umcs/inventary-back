from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from core.schemas.item import Item

router = APIRouter()


@router.get("/list")
def refresh(length: int, skip: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    itemik = Item(id=2, name="item123", category="Potężna kategoria szachowa", value="W ciul ", warehouse="koło",
                  description="Potężny opisik", keywords=['Jeżyk'])
    return [
        itemik
    ]
