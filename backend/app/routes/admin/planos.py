from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.database import supabase
from app.models.validations import Planos

router = APIRouter(prefix="/planos", tags=["planos"])

@router.get("/view")
def get_plans():
    response = supabase.table("planos").select("*").execute()

    return response.data

@router.post("/create")
def create_plan(product: Planos):
    data = jsonable_encoder(product)

    response = supabase.table("planos").insert(data).execute()

    return response.data


