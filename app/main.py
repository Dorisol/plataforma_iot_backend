
from fastapi import FastAPI
from app.core.config import settings
from app.db import base
from app.api.routes import MedicionesRoute
from app.api.routes import AuthRoute
from app.api.routes import TenantsRoute
from app.api.routes import UsuariosRoute
from fastapi.middleware.cors import CORSMiddleware
from app.mqtt.handler import start_mqtt

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

origin = [
    "http://localhost:8000", #swagger 
    "http://localhost:5173", #frontend react
]

#Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Aqui definir las rutas
app.include_router(MedicionesRoute.router, prefix="/plataforma_iot/api", tags=["Mediciones"])
app.include_router(AuthRoute.router, prefix="/plataforma_iot/api", tags=["Auth"])
app.include_router(TenantsRoute.router, prefix="/plataforma_iot/api", tags=["Tenants"])
app.include_router(UsuariosRoute.router, prefix="/plataforma_iot/api", tags=["Usuarios"])

#Aqui recibo los datos de MQTT
@app.on_event("startup")
def iniciar_mqtt():
    print("Iniciando hilo de MQTT...")
    start_mqtt()
    print("Hilo de MQTT iniciado en segundo plano.")
