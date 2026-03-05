from sqlalchemy.orm import Session
from app.models.TenantsModel import Tenant

def get_tenants(db: Session):
    return db.query(Tenant).all()