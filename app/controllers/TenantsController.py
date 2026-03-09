from sqlalchemy.orm import Session
from app.models.TenantsModel import Tenant

def get_tenants(db: Session):
    return db.query(Tenant).all()


#obtener la info del tenant
def get_tenant(db: Session, idTenant: str):
    return db.query(Tenant).filter(Tenant.idTenant == idTenant).first()