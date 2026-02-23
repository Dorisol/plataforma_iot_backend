from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class MedicionesBase(BaseModel):
    variable: str
    val: float
    unit: str
    metadata_medicion: dict | None = None

class Mediciones(MedicionesBase):
    id_medida: UUID
    fk_tenant_id: UUID
    fk_user_id: UUID
    recorded_at: datetime

    class Config:
        from_attributes = True

class MedicionesCreate(MedicionesBase):
    fk_tenant_id: UUID
    fk_user_id: UUID
