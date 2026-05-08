from fastapi import APIRouter
from app.database import supabase
from app.services.auth_services import login_validation, register_validation

router = APIRouter(prefix="/auth")
user_tabel = supabase.table("usuarios").select("*").execute()


@router.post("/login")
def login(email: str, pwd: str):
    response = login_validation(email, pwd)

    return response
    

@router.post("/register")
def register(nome: str, email: str, pwd: str, telefone: str, cpf: str):
    response = register_validation(nome, email, pwd, telefone, cpf)
    supabase.table("usuarios").insert(response).execute()

    return {"msg": "Conta criada com sucesso!"}
    
        
