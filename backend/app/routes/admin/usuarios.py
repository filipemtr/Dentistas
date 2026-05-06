from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database import supabase
from models.validations import Usuarios

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def home_usuarios():
    return {"msg": "usuarios"}

@router.get("/view")
def get_users():
    response = supabase.table("usuarios").select("*").execute()

    return response.data

@router.post("/create")
def create_user(user: Usuarios):
    data = jsonable_encoder(user)
    
    response = supabase.table("usuarios").insert(data).execute()

    return response.data