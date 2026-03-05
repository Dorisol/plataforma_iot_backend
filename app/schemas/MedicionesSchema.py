from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class MedicionesBase(BaseModel):
    variable: str
    val: float
    unit: str
    metadata_medicion: dict | None = None

    class Config:
        from_attributes = True

class Mediciones(MedicionesBase):
    idMedicion: UUID
    idTenant: UUID
    idUsuario: UUID
    recorded_at: datetime

class MedicionesCreate(MedicionesBase):
    idTenant: UUID
    idUsuario: UUID
