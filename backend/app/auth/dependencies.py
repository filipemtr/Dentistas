from fastapi import Depends, HTTPException

def get_current_user():
    user = {"role": "admin"}

    if not user:
        raise HTTPException(401, detail="Não autenticado")
    return user

def is_admin(user = Depends(get_current_user)):
    if user != "admin":
        raise HTTPException(403, detail="Você não tem permissão suficiente.")
    return user