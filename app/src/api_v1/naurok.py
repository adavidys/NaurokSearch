from fastapi import APIRouter


router = APIRouter(prefix="/naurok", tags=["naurok api"])

@router.get("/")
def q():
    return {}