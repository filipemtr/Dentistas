from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.validations import Procedimentos
from app.database import supabase    

router = APIRouter(prefix="/procedimentos", tags=["procedimentos"])

@router.get("/")
def get_procedure():
    response = supabase.table("procedimentos").select("*").execute()

    return response.data

@router.post("/")
def create_procedure(order: Procedimentos):
    data = jsonable_encoder(order)

    response = supabase.table("procedimentos").insert(data).execute()

    return response.data