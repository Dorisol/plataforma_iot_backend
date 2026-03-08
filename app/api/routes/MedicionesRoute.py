from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from sqlalchemy import text
from app.controllers import MedicionesController
from app.schemas import MedicionesSchema
from uuid import UUID

#endpoints
router = APIRouter()

@router.get("/mediciones/todasMediciones", response_model=List[MedicionesSchema.Mediciones])
def get_mediciones(db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones(db)

@router.get("/mediciones/{tenant_id}", response_model=List[MedicionesSchema.Mediciones])
def get_mediciones_tenant(tenant_id: UUID, db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones_tenant(db, tenant_id)

@router.get("/mediciones/{tenant_id}/{usuario_id}", response_model=List[MedicionesSchema.Mediciones])
def get_mediciones_usuario(usuario_id: UUID, tenant_id: UUID, db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones_usuario(db, usuario_id, tenant_id)
