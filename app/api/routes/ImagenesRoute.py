from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from sqlalchemy import text
from app.controllers import ImagenesController
from app.schemas import ImagenesSchema
from uuid import UUID   

router = APIRouter()

@router.get("/imagenes/todasImagenes", response_model=List[ImagenesSchema.ImagenesBase])
def get_todas_imagenes(db: Session = Depends(get_db)):
    return ImagenesController.get_todas_imagenes(db)

@router.get("/imagenes/{idTenant}/{idDispositivo}/", response_model=List[ImagenesSchema.ImagenesBase])
def get_imagenes_dispositivo(idDispositivo: UUID, idTenant: UUID, db: Session = Depends(get_db)):
    return ImagenesController.get_imagenes_dispositivo(db, idDispositivo, idTenant)

