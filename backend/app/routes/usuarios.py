from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.database import supabase
from app.models.validations import Usuarios

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def get_users():
    response = supabase.table("usuarios").select("*").execute()

    return response.data

@router.post("/")
def create_user(user: Usuarios):
    data = jsonable_encoder(user)
    
    response = supabase.table("usuarios").insert(data).execute()

    return response.data