from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.validations import Pedidos
from app.database import supabase    

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/view")
def get_order():
    response = supabase.table("pedidos").select("*").execute()

    return response.data

@router.post("/create")
def create_order(order: Pedidos):
    data = jsonable_encoder(order)

    response = supabase.table("pedidos").insert(data).execute()

    return response.data