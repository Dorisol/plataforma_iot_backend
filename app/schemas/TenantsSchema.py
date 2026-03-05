from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class TenantsSchema(BaseModel):
    idTenant: UUID
    nombre: str
    created_at: datetime
    isActivo: bool

    class Config:
        from_attributes = True