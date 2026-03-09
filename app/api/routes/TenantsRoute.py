
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.controllers import TenantsController
from app.schemas import TenantsSchema
from uuid import UUID

#endpoints
router = APIRouter()

@router.get("/tenants/todosTenants", response_model=List[TenantsSchema.TenantsSchema])
def get_tenants(db: Session = Depends(get_db)):
    return  TenantsController.get_tenants(db)


@router.get("/tenants/{idTenant}", response_model=TenantsSchema.TenantsSchema)
def get_tenant(db: Session = Depends(get_db), idTenant: UUID = None):
    return TenantsController.get_tenant(db, idTenant)