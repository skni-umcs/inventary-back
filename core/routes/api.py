from fastapi import APIRouter
from core.routes.endpoints import loginEndpoint, refreshEndpoint, userEndpoint, itemEndpoint

api_router = APIRouter()

api_router.include_router(loginEndpoint.router)
api_router.include_router(refreshEndpoint.router)

api_router.include_router(userEndpoint.router, prefix='/user', tags=['user'])
api_router.include_router(itemEndpoint.router, prefix='/item', tags=['item'])
