from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class DispositivosBase(BaseModel):
    idTenant: UUID
    username: str
    apiKey: str | None
    rol: str
    isActivo: bool
    protocolo: str | None

    class Config:
        from_attributes = True

class DispositivosCreate(DispositivosBase):
    pass

class DispositivosSchema(DispositivosBase):
    idDispositivo: UUID
    created_at: datetime
