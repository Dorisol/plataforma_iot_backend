from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from .TenantsSchema import TenantsSchema

class UsuarioBase(BaseModel):
    idUsuario: UUID
    username: str
    rol: str
    isActivo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    idTenant: UUID | None
    username: str
    rol: str
    isActivo: bool = True
    password: str

class UsuarioConTenant(UsuarioBase):
    tenant: TenantsSchema | None


