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


# #Obtener la temperatura de un dispositivo de las 24 horas
# def get_temperatura_dispositivo_24hrs(db: Session, idDispositivo: UUID, idTenant: UUID):
#     try:
#         hace_24_horas = datetime.now() - timedelta(hours=24)
#         return db.query(Mediciones).filter(
#             Mediciones.idDispositivo == idDispositivo,
#             Mediciones.idTenant == idTenant,
#             Mediciones.variable == "temperatura",
#             Mediciones.recorded_at >= hace_24_horas
#         ).order_by(Mediciones.recorded_at.desc()).all()
#     except Exception:
#         return []
    
# # Obtener la temperatura de un dispositivo de la última semana (7 días)
# def get_temperatura_dispositivo_semana(db: Session, idDispositivo: UUID, idTenant: UUID):
#     try:
#         hace_una_semana = datetime.now() - timedelta(days=7)
#         return db.query(Mediciones).filter(
#             Mediciones.idDispositivo == idDispositivo,
#             Mediciones.idTenant == idTenant,
#             Mediciones.variable == "temperatura",
#             Mediciones.recorded_at >= hace_una_semana
#         ).order_by(Mediciones.recorded_at.desc()).all()
#     except Exception:
#         return []

# #Obtener la humedad  de un dispositivo de las 24 horas
# def get_humedad_dispositivo_24hrs(db: Session, idDispositivo: UUID, idTenant: UUID):
#     try:
#         hace_24_horas = datetime.now() - timedelta(hours=24)
#         return db.query(Mediciones).filter(
#             Mediciones.idDispositivo == idDispositivo,
#             Mediciones.idTenant == idTenant,
#             Mediciones.variable == "humedad",
#             Mediciones.recorded_at >= hace_24_horas
#         ).order_by(Mediciones.recorded_at.desc()).all()
#     except Exception:
#         return []

# #obtener la humedad del un dispositivo de la semana 
# def get_humedad_dispositivo_semana(db: Session, idDispositivo: UUID, idTenant: UUID):
#     try:
#         hace_una_semana = datetime.now() - timedelta(days=7)
#         return db.query(Mediciones).filter(
#             Mediciones.idDispositivo == idDispositivo,
#             Mediciones.idTenant == idTenant,
#             Mediciones.variable == "humedad",
#             Mediciones.recorded_at >= hace_una_semana
#         ).order_by(Mediciones.recorded_at.desc()).all()
#     except Exception:
#         return []

def get_mediciones_por_rango(db: Session, idTenant: UUID, idDispositivo: UUID, rango: str):
    try:
        #primero determinar el límite de tiempo
        if rango == "24h":
            limite_tiempo = datetime.now() - timedelta(hours=24)
        else:
            limite_tiempo = datetime.now() - timedelta(days=7)
        
        return db.query(Mediciones).filter(
            Mediciones.idTenant == idTenant,
            Mediciones.idDispositivo == idDispositivo,
            Mediciones.recorded_at >= limite_tiempo
        ).order_by(Mediciones.recorded_at.asc()).all()

    except Exception as e:
        print("Error al obtener las mediciones por rango: ", e)
        return []