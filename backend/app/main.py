from fastapi import FastAPI, Depends, APIRouter
from auth.dependencies import is_admin
from backend.app.routes.admin import consultas, pacientes, pedidos, planos, procedimentos, usuarios

app = FastAPI(title="dentistas_backend")

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


