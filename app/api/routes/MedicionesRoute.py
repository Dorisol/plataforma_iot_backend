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

@router.get("/mediciones/{tenant_id}/{dispositivo_id}", response_model=List[MedicionesSchema.MedicionAgrupada])
def get_mediciones_por_rango(tenant_id: UUID, dispositivo_id: UUID,  rango: str = "7d", db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones_por_rango(db, tenant_id, dispositivo_id, rango)



#-------------------------------------------------------------------------------------------------------------------    

# @router.get("/mediciones/temperatura/24hrs/{tenant_id}/{dispositivo_id}", response_model=List[MedicionesSchema.Mediciones])
# def get_temperatura_dispositivo_24hrs(tenant_id: UUID, dispositivo_id: UUID, db: Session = Depends(get_db)):
#     return MedicionesController.get_temperatura_dispositivo_24hrs(db, dispositivo_id, tenant_id)

# @router.get("/mediciones/temperatura/semana/{tenant_id}/{dispositivo_id}", response_model=List[MedicionesSchema.Mediciones])
# def get_temperatura_dispositivo_semana(tenant_id: UUID, dispositivo_id: UUID, db: Session = Depends(get_db)):
#     return MedicionesController.get_temperatura_dispositivo_semana(db, dispositivo_id, tenant_id)

# @router.get("/mediciones/humedad/24hrs/{tenant_id}/{dispositivo_id}", response_model=List[MedicionesSchema.Mediciones])
# def get_humedad_dispositivo_24hrs(tenant_id: UUID, dispositivo_id: UUID, db: Session = Depends(get_db)):
#     return MedicionesController.get_humedad_dispositivo_24hrs(db, dispositivo_id, tenant_id)

# @router.get("/mediciones/humedad/semana/{tenant_id}/{dispositivo_id}", response_model=List[MedicionesSchema.Mediciones])
# def get_humedad_dispositivo_semana(tenant_id: UUID, dispositivo_id: UUID, db: Session = Depends(get_db)):
#     return MedicionesController.get_humedad_dispositivo_semana(db, dispositivo_id, tenant_id)

