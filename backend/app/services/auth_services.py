from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from auth.jwt import verify_password, create_token, hash_password
from models.validations import Register
from database import supabase
from config import allowed_email

user_tabel = supabase.table("usuarios").select("*").execute()

def login_validation(email: str, pwd: str):
    response = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .execute()
    )

    user = response.data[0] if response.data else None

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Usuário não encontrado"
        )
    
    if not verify_password(pwd, user["senha"]):
        raise HTTPException(400, "Senha incorreta!")

    token = create_token({
        "sub": str(user["id"]),
        "role": str(user["role"])
    })
    
    return {
        "acess_token": token,
        "token_type": "bearer"
    }

def register_validation(obj: Register):
    new_user = {
        "email": obj.email,
        "senha": hash_password(obj.senha),
        "role": "paciente" 
    }

    return new_user
        