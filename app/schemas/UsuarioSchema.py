from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UsuarioBase(BaseModel):
    idTenant: UUID
    username: str
    rol: str
    isActivo: bool

    class Config:
        from_attributes = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioSchema(UsuarioBase):
    idUsuario: UUID
    created_at: datetime