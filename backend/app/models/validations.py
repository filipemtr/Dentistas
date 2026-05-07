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

class Consultas(BaseModel):
    id: int
    paciente_id: UUID
    procedimento_id: int
    plano_id: int
    data: datetime
    data_criada: datetime
    e_ativo: bool
    valor: float

class Pacientes(BaseModel):
    id: UUID
    cpf: str
    nome: str
    telefone: str

class Procedimentos(BaseModel):
    id: int
    nome: str
    custo: float

class Register(BaseModel):
    email: str
    senha: str