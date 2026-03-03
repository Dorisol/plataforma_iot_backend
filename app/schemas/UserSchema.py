from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserSchema(BaseModel):
    id_user: UUID
    fk_tenant_id: UUID
    username: str
    password_hash: str
    api_key: str | None
    role: str
    is_active: bool
    created_at: datetime