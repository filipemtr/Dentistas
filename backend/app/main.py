from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from auth.dependencies import is_admin
from routes.admin import consultas, pacientes, pedidos, planos, procedimentos, usuarios
from routes.public import home, auth

app = FastAPI(title="dentistas_backend")

@app.get("/")
def startview():
    return "Bem vindo ao site da clínica!"

admin_router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(is_admin)]
)

admin_router.include_router(consultas.router)
admin_router.include_router(pacientes.router)
admin_router.include_router(pedidos.router)
admin_router.include_router(planos.router)
admin_router.include_router(procedimentos.router)
admin_router.include_router(usuarios.router)

app.include_router(admin_router)
app.include_router(home.router)
app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






