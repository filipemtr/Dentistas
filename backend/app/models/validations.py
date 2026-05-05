from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Pedidos(BaseModel):
    plano: int
    feito_em: datetime
    id_pacientes: UUID

class Planos(BaseModel):
    nome_plano: str
    desconto: float
    preco: float

class Usuarios(BaseModel):
    id: UUID
    nome: str
    role: str
    telefone: str
    criado_em: datetime