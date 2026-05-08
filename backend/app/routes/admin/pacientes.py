from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.validations import Pacientes
from app.services.pacientes_service import create_person
from app.database import supabase    

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
    data = create_person(order)

    return data