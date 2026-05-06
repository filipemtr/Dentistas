from fastapi import APIRouter

router = APIRouter(prefix="/home")

@router.get("/")
def home():
    return {"msg": "página principal"}
