
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