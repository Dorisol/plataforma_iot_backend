from sqlalchemy.orm import Session
from app.models.ImagenesModel import Imagenes
from uuid import UUID
from app.schemas.ImagenesSchema import ImagenesBase

def get_todas_imagenes(db: Session):
    return db.query(Imagenes).all()

def get_imagenes_dispositivo(db: Session, idDispositivo: UUID, idTenant: UUID):
    return db.query(Imagenes).filter(Imagenes.idDispositivo == idDispositivo, Imagenes.idTenant == idTenant).all()



