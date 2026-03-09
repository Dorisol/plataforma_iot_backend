from sqlalchemy import Column, ForeignKey, Uuid, String, Boolean, TIMESTAMP
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Dispositivos(Base):
    __tablename__ = "dispositivos"
    idDispositivo = Column(Uuid, primary_key=True, index=True)
    idTenant = Column(Uuid, ForeignKey("tenants.idTenant"))
    username = Column(String, unique=True, index=True)
    apiKey = Column(String)
    rol = Column(String)
    isActivo = Column(Boolean, default=True)
    protocolo = Column(String)
    imagenesDisponibles = Column(Boolean)
    created_at = Column(TIMESTAMP)

    #Relaciones
    #(nombre del modelo relacionado, nombre del campo que va a estar relacionado en el otro modelo)
    #en ese caso, "dispositivos" debe definirse en el modelo Tenant
    tenant = relationship("Tenant", back_populates="dispositivos")
    medicion = relationship("Mediciones", back_populates="dispositivo")
