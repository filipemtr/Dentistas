from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from auth.jwt import verify_password, create_token, hash_password
from models.validations import Register
from database import supabase
from config import allowed_email

user_tabel = supabase.table("usuarios").select("*").execute()
symbols = "/,.;~]´[=-'#$%¨&*(){}_"

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
    
    response_body = {
        "acess_token": token,
        "token_type": "bearer"
    }

    return response_body

def register_validation(nome: str, email: str, pwd: str, tel: str, cpf: str):
    for symbol in symbols:
        if symbol in nome:
            raise HTTPException(400, "Nome inválido!")
    if "@" not in email or "." not in email:
        raise HTTPException(400, "Email inválido!")
    if len(pwd) < 8:
        raise HTTPException(400, "Senha precisa ter mais de 8 caracteres.")
    if len(cpf) != 11:
        cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")
        if len(cpf) != 11:
            raise HTTPException(400, "CPF Inválido!")
    
    validation = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if validation.data:
        raise HTTPException(400, "Email já  já existente!")
    
    validation = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("cpf", cpf)
        .execute()
    )

    if validation.data:
        raise HTTPException(400, "CPF já existente!")

    new_user = {
        "nome": nome,
        "email": email,
        "senha": hash_password(pwd),
        "telefone": tel,
        "cpf": cpf,
        "role": "paciente" 
    }

    return new_user
        