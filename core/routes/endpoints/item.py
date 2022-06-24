from fastapi import APIRouter
from core.routes.endpoints.item_ import list

router = APIRouter()

router.include_router(list.router)
