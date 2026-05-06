from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database import supabase
from models.validations import Planos

router = APIRouter(prefix="/planos", tags=["planos"])

@router.get("/")
def home_planos():
    return {"msg": "planos"}

@router.get("/view")
def get_plans():
    response = supabase.table("planos").select("*").execute()

    return response.data

@router.post("/create")
def create_plan(product: Planos):
    data = jsonable_encoder(product)

    response = supabase.table("planos").insert(data).execute()

    return response.data


