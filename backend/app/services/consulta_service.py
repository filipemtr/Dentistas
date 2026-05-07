from fastapi import HTTPException
from database import supabase

def create_appoint(data: dict):
    
    # validar paciente

    paciente = (
        supabase
        .table("pacientes")
        .select("*")
        .eq("id", data["paciente_id"])
        .execute()
    )

    if not paciente.data:
        raise HTTPException(
            404,
            "Paciente não encontrado"
        )

    # validar consulta

    consulta_existente = (
        supabase
        .table("consultas")
        .select("*")
        .eq("data", data["data"])
        .execute()
    )

    if consulta_existente.data:
        raise HTTPException(
            400,
            "Horário ocupado"
        )
    
    # criar de fato

    response = (
        supabase
        .table("consultas")
        .insert(data)
        .execute()
    )

    return response.data