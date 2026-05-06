from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.validations import Procedimentos
from database import supabase    

router = APIRouter(prefix="/procedimentos", tags=["procedimentos"])

@router.get("/")
def home_procedimentos():
    return {"msg": "procedimentos"}

@router.get("/view")
def get_procedure():
    response = supabase.table("procedimentos").select("*").execute()

    return response.data

@router.post("/create")
def create_procedure(order: Procedimentos):
    data = jsonable_encoder(order)

    response = supabase.table("procedimentos").insert(data).execute()

    return response.data