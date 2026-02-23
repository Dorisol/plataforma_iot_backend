
from fastapi import FastAPI
from app.core.config import settings
import threading
from app.db import base
from app.api.routes import MedicionesRoute
from app.mqtt.handler import start_mqtt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

origin = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(MedicionesRoute.router, prefix="/api/mediciones", tags=["Mediciones"])

@app.on_event("startup")
def startup_event():
    print("Iniciando hilo de MQTT...")
    start_mqtt()
    print("Hilo de MQTT iniciado en segundo plano.")