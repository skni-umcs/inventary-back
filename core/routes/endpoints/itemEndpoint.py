from fastapi import APIRouter
from core.routes.endpoints.itemEndpoints import list

router = APIRouter()

router.include_router(list.router)
