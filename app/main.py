
from fastapi import FastAPI
from app.core.config import settings
import threading
from app.db import base
from app.api.routes import MedicionesRoute
from app.api.routes import AuthRoute
from app.mqtt.handler import start_mqtt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

origin = [
    "http://localhost:3000",
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
app.include_router(MedicionesRoute.router, prefix="/api/Mediciones", tags=["Mediciones"])
app.include_router(AuthRoute.router, prefix="/api/Auth", tags=["Auth"])

#Para MQTT (PENDIENTE)
@app.on_event("startup")
def startup_event():
    print("Iniciando hilo de MQTT...")
    start_mqtt()
    print("Hilo de MQTT iniciado en segundo plano.")