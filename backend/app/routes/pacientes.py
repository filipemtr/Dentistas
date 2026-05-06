from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.validations import Pacientes
from app.database import supabase    

router = APIRouter(prefix="/pacientes", tags=["pacientes"])

@router.get("/")
def get_pacients():
    response = supabase.table("pacientes").select("*").execute()

    return response.data

@router.post("/")
def create_pacient(order: Pacientes):
    data = jsonable_encoder(order)

    response = supabase.table("pacientes").insert(data).execute()

    return response.data