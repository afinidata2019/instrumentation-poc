from fastapi import APIRouter

from api.endpoints import resources


router = APIRouter()


router.include_router(resources.router, prefix="/resources")
