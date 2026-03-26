from sqlalchemy.orm import Session
from app.models.DispositivosModel import Dispositivos
from app.schemas import DispositivosSchema
from uuid import UUID
from fastapi import HTTPException

#traer todos los dispositivos del tenant 
def get_dispositivos(db: Session, idTenant: UUID):
    return db.query(Dispositivos).filter(Dispositivos.idTenant == idTenant).all()

def get_todos_dispositivos(db: Session):
    return db.query(Dispositivos).all()


#agregar un nuevo dispositivo
def crearUsuario(db: Session, nuevoDispositivo: DispositivosSchema.DispositivosCreate):
    try:
        nuevo_dispositivo = Dispositivos(
            idTenant=nuevoDispositivo.idTenant,
            username=nuevoDispositivo.username,
            apiKey=None,
            rol=nuevoDispositivo.rol,
            isActivo=nuevoDispositivo.isActivo,
            protocolo=nuevoDispositivo.protocolo,
            imagenesDisponibles=nuevoDispositivo.imagenesDisponibles
        )
        db.add(nuevo_dispositivo)
        db.commit()
        db.refresh(nuevo_dispositivo)
        return nuevo_dispositivo
    
    except Exception as e:
        db.rollback() 
        print("Error real en la BD: ", str(e))
        raise HTTPException(status_code=400, detail=f"Error en BD: {str(e)}")