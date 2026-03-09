from sqlalchemy.orm import Session
from app.models.MedicionesModel import Mediciones
from uuid import UUID

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
    

    

    