from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class UserBase(BaseModel):
    username: str

class User(UserBase):
    id_user: UUID
    fk_tenant_id: UUID
    password_hash: str
    api_key: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass