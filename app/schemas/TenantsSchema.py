from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class TenantBase(BaseModel):
    name: str

class Tenant(TenantBase):
    id_tenant: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TenantCreate(TenantBase):
    pass #no necesita campos adicionales
