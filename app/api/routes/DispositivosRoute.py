from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.controllers import DispositivosController
from app.schemas import DispositivosSchema
from uuid import UUID

#endpoints
router = APIRouter()

@router.get("/dispositivos/todosDispositivos", response_model=List[DispositivosSchema.DispositivosSchema])
def get_todos_dispositivos(db: Session = Depends(get_db)):
    return DispositivosController.get_todos_dispositivos(db)

@router.get("/dispositivos/{idTenant}", response_model=List[DispositivosSchema.DispositivosSchema])
def get_dispositivos(db: Session = Depends(get_db), idTenant: UUID = None):
    return DispositivosController.get_dispositivos(db, idTenant)

@router.post("/dispositivos/crearDispositivo", response_model=DispositivosSchema.DispositivosSchema)
def crearDispositivo(dispositivo_data: DispositivosSchema.DispositivosCreate, db: Session = Depends(get_db)):
    return DispositivosController.crearUsuario(db, dispositivo_data)
