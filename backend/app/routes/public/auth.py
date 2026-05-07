from fastapi import APIRouter
from database import supabase
from fastapi import HTTPException
from models.validations import Register
from auth.jwt import hash_password, verify_password, create_token
from services.auth_services import login_validation, register_validation

router = APIRouter(prefix="/auth")
user_tabel = supabase.table("usuarios").select("*").execute()


@router.post("/login")
def login(email: str, pwd: str):
    response = login_validation

    return response
    

@router.post("/register")
def register(data: Register):

    response = register_validation(data)

    supabase.table("usuarios").insert(response).execute()
    
    return {"msg": "Sucesso!"}
    
        
