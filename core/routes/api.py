from fastapi import APIRouter
from core.routes.endpoints import loginEndpoint, refreshEndpoint, userEndpoint, itemEndpoint, categoryEndpoint, registerEndpoint
from core.routes.endpoints import warehouseEndpoint

api_router = APIRouter()

api_router.include_router(loginEndpoint.router)
api_router.include_router(refreshEndpoint.router)

api_router.include_router(userEndpoint.router, prefix='/user', tags=['user'])
api_router.include_router(itemEndpoint.router, prefix='/item', tags=['item'])
api_router.include_router(categoryEndpoint.router, prefix='/category', tags=['category'])
api_router.include_router(warehouseEndpoint.router, prefix='/warehouse', tags=['warehouse'])
api_router.include_router(registerEndpoint.router, prefix='/register', tags=['registration'])
