from sqlalchemy import Column, ForeignKey, Uuid, String, Boolean, TIMESTAMP
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    id_user = Column(Uuid, primary_key=True, index=True)
    fk_tenant_id = Column(Uuid, ForeignKey("tenants.id_tenant"))
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    api_key = Column(String)
    role = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)

    #Relaciones
    #(nombre del modelo relacionado, nombre del campo que va a estar relacionado en el otro modelo)
    #en ese caso, "users debe definirse en el modelo Tenant "
    tenant = relationship("Tenant", back_populates="user")
    medicion = relationship("Mediciones", back_populates="user_med")
