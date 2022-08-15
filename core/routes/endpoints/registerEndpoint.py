from fastapi import APIRouter, HTTPException, Depends
from core.schemas import UserSchema
from fastapi_jwt_auth import AuthJWT
import core.db.userDb as UD
from core.routes.endpoints.registerTokenEndpoints import token as tokenEndpoint
from .. import get_db_session, Session
import core.logic.registration as RL

router = APIRouter()

router.include_router(tokenEndpoint.router, prefix='/token')


@router.post('')
def register(token: str, user: UserSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    if Authorize.get_jwt_subject():
        HTTPException(status_code=401, detail="Already logged in")

    if UD.get_by_username(session, user.username):
        raise HTTPException(status_code=422, detail="Username already exists")

    if user.password != user.password_repeat:
        raise HTTPException(status_code=422, detail="Passwords don't match")

    try:
        tokenSchema = RL.get_valid_token(session, token)
    except AssertionError:
        raise HTTPException(status_code=422, detail="Invalid token")
    else:
        if not tokenSchema:
            raise HTTPException(status_code=422, detail="Token limit reached")

    try:
        RL.validate_user(session, user)
    except AssertionError:
        raise HTTPException(status_code=422, detail="User validation not passed")

    RL.registerUser(session, tokenSchema, user)

    return {"message": "OK"}

