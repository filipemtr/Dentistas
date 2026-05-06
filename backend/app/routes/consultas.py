from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.validations import Consultas
from app.database import supabase    

router = APIRouter(prefix="/consultas", tags=["consultas"])

@router.get("/view")
def get_appointments():
    response = supabase.table("consultas").select("*").execute()

    return response.data

@router.post("/create")
def create_appointment(order: Consultas):
    data = jsonable_encoder(order)

    response = supabase.table("consultas").insert(data).execute()

    return response.data