from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os


pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(pwd: str):
    return pwd_context.hash(pwd)

def verify_password(pwd: str, hashed:str):
    return pwd_context.verify(pwd, hashed)

def create_token(data: dict):
    diference_time = os.getenv("ACESS_TOKEN_EXPIRE_MINUTES")
    validation_time = datetime.now(timezone.utc) + timedelta(minutes=int(diference_time))

    KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

    encode_data = data.copy()
    encode_data["exp"] = validation_time

    return jwt.encode(encode_data, KEY, ALGORITHM)

