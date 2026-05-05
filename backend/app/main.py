from fastapi import FastAPI
from app.routes import usuarios, planos, pedidos

app = FastAPI(title="dentistas_backend")

app.include_router(usuarios.router)
app.include_router(planos.router)
app.include_router(pedidos.router)