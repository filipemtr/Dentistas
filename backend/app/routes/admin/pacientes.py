from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.validations import Pacientes
from database import supabase    

router = APIRouter(prefix="/pacientes", tags=["pacientes"])

@router.get("/")
def home_pacientes():
    return {"msg": "pacientes"}


@router.get("/view")
def get_pacients():
    response = supabase.table("pacientes").select("*").execute()

    return response.data

@router.post("/create")
def create_pacient(order: Pacientes):
    data = jsonable_encoder(order)

    response = supabase.table("pacientes").insert(data).execute()

    return response.data