from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.categoryDb as CD

router = APIRouter()


@router.get("/all")
def get_all_categories(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    categorySchemes = CD.get_all()

    return categorySchemes
