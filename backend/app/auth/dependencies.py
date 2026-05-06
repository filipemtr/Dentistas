from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2scheme)):
    try:
        KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")

        payload = jwt.decode(token, KEY, [ALGORITHM])
        user_id = payload.get("sub")
        role = payload.get("role")

        if user_id is None:
            raise HTTPException(401, "Token inválido!")

        user = {
            "user_id": user_id,
            "role": role
        }

        return user

    except (JWTError, HTTPException):
        raise HTTPException(401, "Token inválido!")

def is_admin(user = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(403, detail="Você não tem permissão suficiente.")
    return user

def is_pacient(user = Depends(get_current_user)):
    if user["role"] != "paciente":
        raise HTTPException(403, detail="Você não tem permissão suficiente.")
    return user