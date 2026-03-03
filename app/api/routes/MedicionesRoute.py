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

@router.get("/todasMediciones", response_model=List[MedicionesSchema.Mediciones])
def get_mediciones(db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones(db)

@router.get("/mediciones/{tenant_id}", response_model=List[MedicionesSchema.Mediciones])
def get_mediciones_tenant(tenant_id: UUID, db: Session = Depends(get_db)):
    return MedicionesController.get_mediciones_tenant(db, tenant_id)



# @router.get("/{tenant_id}")
# def get_mediciones(tenant_id: str, db: Session = Depends(get_db)):
#     query = text("SELECT * FROM mediciones WHERE fk_tenant_id = :t_id")
#     result = db.execute(query, {"t_id": tenant_id})
#     return [dict(row._mapping) for row in result]