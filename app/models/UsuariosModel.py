from sqlalchemy import Column, ForeignKey, Uuid, String, Boolean, TIMESTAMP
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Usuarios(Base):
    __tablename__ = "usuarios"
    idUsuario = Column(Uuid, primary_key=True, index=True)
    idTenant = Column(Uuid, ForeignKey("tenants.idTenant"))
    username = Column(String, unique=True, index=True)
    password = Column(String)
    apiKey = Column(String)
    rol = Column(String)
    isActivo = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)

    #Relaciones
    #(nombre del modelo relacionado, nombre del campo que va a estar relacionado en el otro modelo)
    #en ese caso, "users debe definirse en el modelo Tenant "
    tenant = relationship("Tenant", back_populates="usuario")
    medicion = relationship("Mediciones", back_populates="usuario_med")
