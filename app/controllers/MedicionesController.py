from sqlalchemy.orm import Session
from app.models.MedicionesModel import Mediciones
from uuid import UUID

def get_mediciones(db: Session):
    return db.query(Mediciones).all()

def get_mediciones_tenant(db: Session, tenant_id: UUID):
    try: 
        return db.query(Mediciones).filter(Mediciones.fk_tenant_id == tenant_id).all()
    except Exception:
        return []


# cdd98751-bc77-4741-af8a-16cfbbb99a22

# def save_medicion(db: Session, data: dict, tenant_id: str, user_id: str):
#     db_medicion = Mediciones(
#         fk_tenant_id=tenant_id,
#         fk_user_id=user_id,
#         variable=data.get("variable"),
#         val=data.get("val"),
#         unit=data.get("unit"),
#         metadata={"device": user_id}
#     )
#     db.add(db_medicion)
#     db.commit()
#     return db_medicion