from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.auth.jwt import verify_password, create_token, hash_password
from app.models.validations import Register
from app.database import supabase

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

def register_validation(instance: Register):
    for symbol in symbols:
        if symbol in instance.nome:
            raise HTTPException(400, "Nome inválido!")
    if "@" not in instance.email or "." not in instance.email:
        raise HTTPException(400, "Email inválido!")
    if len(instance.pwd) < 8:
        raise HTTPException(400, "Senha precisa ter mais de 8 caracteres.")
    if len(instance.cpf) != 11:
        instance.cpf = instance.cpf.replace(".", "").replace("-", "").replace(" ", "")
        if len(instance.cpf) != 11:
            raise HTTPException(400, "CPF Inválido!")
    
    validation = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("email", instance.email)
        .execute()
    )

    if validation.data:
        raise HTTPException(400, "Email já  já existente!")
    
    validation = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("cpf", instance.cpf)
        .execute()
    )

    if validation.data:
        raise HTTPException(400, "CPF já existente!")

    new_user = {
        "nome": instance.nome,
        "email": instance.email,
        "senha": hash_password(instance.pwd),
        "telefone": instance.telefone,
        "cpf": instance.cpf,
        "role": "paciente" 
    }

    return new_user
        