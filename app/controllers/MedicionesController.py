from sqlalchemy.orm import Session
from app.models.MedicionesModel import Mediciones
from uuid import UUID
from datetime import datetime, timedelta

def get_mediciones(db: Session):
    return db.query(Mediciones).all()

def get_mediciones_tenant(db: Session, idTenant: UUID):
    try: 
        return db.query(Mediciones).filter(Mediciones.idTenant == idTenant).all()
    except Exception:
        return []
    
def get_mediciones_usuario(db: Session, idDispositivo: UUID, idTenant: UUID):
    try:
        return db.query(Mediciones).filter(Mediciones.idDispositivo == idDispositivo, Mediciones.idTenant == idTenant).all()       
    except Exception:
        return []


#Obtener la temperatura de un dispositivo de las 24 horas
def get_temperatura_dispositivo_24hrs(db: Session, idDispositivo: UUID, idTenant: UUID):
    try:
        hace_24_horas = datetime.now() - timedelta(hours=24)
        return db.query(Mediciones).filter(
            Mediciones.idDispositivo == idDispositivo,
            Mediciones.idTenant == idTenant,
            Mediciones.variable == "temperatura",
            Mediciones.recorded_at >= hace_24_horas
        ).order_by(Mediciones.recorded_at.desc()).all()
    except Exception:
        return []
    
# Obtener la temperatura de un dispositivo de la última semana (7 días)
def get_temperatura_dispositivo_semana(db: Session, idDispositivo: UUID, idTenant: UUID):
    try:
        hace_una_semana = datetime.now() - timedelta(days=7)
        return db.query(Mediciones).filter(
            Mediciones.idDispositivo == idDispositivo,
            Mediciones.idTenant == idTenant,
            Mediciones.variable == "temperatura",
            Mediciones.recorded_at >= hace_una_semana
        ).order_by(Mediciones.recorded_at.desc()).all()
    except Exception:
        return []

#Obtener la temperatura de un dispositivo de las 24 horas
def get_humedad_dispositivo_24hrs(db: Session, idDispositivo: UUID, idTenant: UUID):
    try:
        hace_24_horas = datetime.now() - timedelta(hours=24)
        return db.query(Mediciones).filter(
            Mediciones.idDispositivo == idDispositivo,
            Mediciones.idTenant == idTenant,
            Mediciones.variable == "humedad",
            Mediciones.recorded_at >= hace_24_horas
        ).order_by(Mediciones.recorded_at.desc()).all()
    except Exception:
        return []

