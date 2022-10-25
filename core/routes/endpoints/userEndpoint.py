from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.get('/')
def user(Authorize: AuthJWT = Depends()):
    # Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

