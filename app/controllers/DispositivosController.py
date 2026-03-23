from sqlalchemy.orm import Session
from app.models.DispositivosModel import Dispositivos
from uuid import UUID

#traer todos los dispositivos del tenant 
def get_dispositivos(db: Session, idTenant: UUID):
    return db.query(Dispositivos).filter(Dispositivos.idTenant == idTenant).all()

def get_todos_dispositivos(db: Session):
    return db.query(Dispositivos).all()