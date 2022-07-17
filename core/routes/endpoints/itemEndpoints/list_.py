from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
import core.db.itemDb as ID
from ... import get_db_session, Session

router = APIRouter()


@router.get("/list")
def get_list_of_items(length: int, skip: int, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    items = ID.get_list(session, length, skip)

    return items
