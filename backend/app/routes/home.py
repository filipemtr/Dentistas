from fastapi import APIRouter

router = APIRouter(prefix="/home")

@router.get("/")
def home():
    return {"msg": "página principal"}

@router.post("/register")
def register():
    return {"msg": "criar conta"}

@router.post("/login")
def login():
    return {"token": "fake-jwt"}