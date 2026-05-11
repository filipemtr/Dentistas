from fastapi import APIRouter
from app.database import supabase
from app.services.auth_services import login_validation, register_validation
from app.models.validations import Register

router = APIRouter(prefix="/auth")
user_tabel = supabase.table("usuarios").select("*").execute()


@router.post("/login")
def login(email: str, pwd: str):
    response = login_validation(email, pwd)

    return response
    

@router.post("/register")
def register(register: Register):
    response = register_validation(register)
    supabase.table("usuarios").insert(response).execute()

    return {"msg": "Conta criada com sucesso!"}
    
        
