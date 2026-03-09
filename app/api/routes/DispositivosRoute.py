from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.controllers import DispositivosController
from app.schemas import DispositivosSchema
from uuid import UUID

#endpoints
router = APIRouter()

#usuarios que NO SON ADMIN NI SUPER_ADMIN
@router.get("/dispositivos/{idTenant}", response_model=List[DispositivosSchema.DispositivosSchema])
def get_dispositivos(db: Session = Depends(get_db), idTenant: str = None):
    return DispositivosController.get_dispositivos(db, idTenant)

