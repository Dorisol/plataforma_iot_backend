from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class DispositivosBase(BaseModel):
    idTenant: UUID
    username: str
    apiKey: Optional[str] = None
    rol: str
    isActivo: bool = True
    protocolo: str | None
    imagenesDisponibles: bool
    created_at: datetime

    class Config:
        from_attributes = True

class DispositivosCreate(BaseModel):
    idTenant: UUID
    username: str
    rol: str
    isActivo: bool = True
    protocolo: str | None
    imagenesDisponibles: bool
    
class DispositivosSchema(DispositivosBase):
    idDispositivo: UUID
    

