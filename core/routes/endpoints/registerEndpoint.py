from fastapi import APIRouter, HTTPException, Depends
from core.schemas import UserSchema
from fastapi_jwt_auth import AuthJWT
import core.db.userDb as UD
from core.routes.endpoints.registerTokenEndpoints import token
from .. import get_db_session, Session

router = APIRouter()

router.include_router(token.router, prefix='/token')


@router.post('/')
def register(token: str, user: UserSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    try:
        userDB = UD.get_by_username(session, user.username)
    except AttributeError:
        pass
    else:
        HTTPException(status_code=401, detail="Username already exists")

    if user.password != user.password_repeat:
        raise HTTPException(status_code=401, detail="Passwords don't match")

    # RTD.get

    return {"message": "NotImplementedYet lulz"}

