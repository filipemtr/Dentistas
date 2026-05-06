from fastapi import APIRouter

router = APIRouter(prefix="/home")

@router.get("/")
def home():
    return {"msg": "página principal"}

@router.get("/register")
def register():
    return {"msg": "criar conta"}

@router.get("/login")
def login():
    return {"token": "fake-jwt"}