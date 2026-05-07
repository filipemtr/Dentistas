from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from models.validations import Consultas
from auth.dependencies import is_admin
from services.consulta_service import create_appoint
from database import supabase    

router = APIRouter(prefix="/consultas", tags=["consultas"])

@router.get("/")
def home_consultas():
    return {"msg": "consultas"}

@router.get("/view")
def get_appointments(user=Depends(is_admin)):
    response = supabase.table("consultas").select("*").execute()

    return response.data

@router.post("/create")
def create_appointment(order: Consultas):
    return create_appoint(order)