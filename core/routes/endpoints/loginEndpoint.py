from fastapi import APIRouter, HTTPException, Depends
from core.schemas import UserSchema
from fastapi_jwt_auth import AuthJWT
from datetime import timedelta

router = APIRouter()


@router.post('/login')
def login(user: UserSchema, Authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.username, expires_time=timedelta(minutes=15), fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=user.username)

    return {"message": "OK",
            "token": access_token,
            "refresh_token": refresh_token}

