from sqlalchemy import Column, Uuid, String, Boolean, TIMESTAMP
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Tenant(Base):
    __tablename__ = "tenants"
    id_tenant = Column(Uuid, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)
    

    #(nombre del modelo relacionado, nombre del campo que va a estar relacionado en el otro modelo)
    #en ese caso, "tenants" debe definirse en el modelo User
    user = relationship("Users", back_populates="tenant")
    medicion = relationship("Mediciones", back_populates="tenant_med")