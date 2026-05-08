from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.database import supabase

def create_person(data:dict):
    
    response = (
        supabase
        .table("pacientes")
        .select("*")
        .eq("cpf", data["cpf"])
        .execute()
    )

    if not response.data:
        data = jsonable_encoder(data)

        response = supabase.table("pacientes").insert(data).execute()
        return response.data