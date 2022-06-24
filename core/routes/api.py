from fastapi import APIRouter
from core.routes.endpoints import login, refresh, user, item

api_router = APIRouter()

api_router.include_router(login.router)
api_router.include_router(refresh.router)

api_router.include_router(user.router, prefix='/user', tags=['user'])
api_router.include_router(item.router, prefix='/item', tags=['item'])
