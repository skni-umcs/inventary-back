from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.categoryDb as CD
from ... import get_db_session, Session

router = APIRouter()


@router.get("/all")
def get_all_categories(Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    categorySchemes = CD.get_all(session)

    return categorySchemes
