from sqlalchemy.orm import Session
from app.models.DispositivosModel import Dispositivos

#traer todos los dispositivos 
def get_dispositivos(db: Session, idTenant: str):
    return db.query(Dispositivos).filter(Dispositivos.idTenant == idTenant).all()