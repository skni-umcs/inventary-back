from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from datetime import timedelta

router = APIRouter()


@router.get("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    access_token = Authorize.create_access_token(subject=current_user, fresh=False, expires_time=timedelta(days=30))

    return {"token": access_token}

