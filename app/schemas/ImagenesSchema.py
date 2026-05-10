from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ImagenesBase(BaseModel):
    idImagen: UUID
    idTenant: UUID
    idDispositivo: UUID
    rutaImg: str
    created_at: datetime

    class Config:
        from_attributes = True

class ImagenesCreate(BaseModel):
    idTenant: UUID
    idDispositivo: UUID
    rutaImg: str


