from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
import core.db.registrationTokenDb as RTD
import core.db.userDb as UD
from ... import get_db_session, Session
import core.logic.registrationTokens as RTL
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.get("/generate")
def generate_token(name: str, userLimit: int, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    try:
        token = RTL.generate_token(session, name, userLimit, current_user)
    except IntegrityError:
        raise HTTPException(status_code=422, detail="This name is already in use for token (most probably :P)")

    return {
        'message': 'OK',
        'token': token
    }


@router.get("/my")
def get_my_tokens(Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()
    userSchema = UD.get_by_username(session, username)

    tokenSchemas = RTD.get_by_creator_id(session, userSchema.id)

    return {
        "message": "OK",
        "tokens": tokenSchemas
    }
