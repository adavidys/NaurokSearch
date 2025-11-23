from fastapi import APIRouter

from .naurok import router as naurok_router


api_v1 = APIRouter(prefix="/api_v1")
api_v1.include_router(naurok_router)