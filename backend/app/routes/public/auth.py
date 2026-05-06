from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.get("/login")
def home():
    return {"msg": "login"}

@router.get("/register")
def home():
    return {"msg": "register"}
