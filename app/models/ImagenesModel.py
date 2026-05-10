from sqlalchemy import Column, ForeignKey, Uuid, String, Boolean, DateTime
from app.db.base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, func
import uuid

class Imagenes(Base):
    __tablename__ = "imagenes"
    idImagen = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    idTenant = Column(Uuid, ForeignKey("tenants.idTenant"))
    idDispositivo = Column(Uuid, ForeignKey("dispositivos.idDispositivo"))
    rutaImg = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    #Relaciones
    #(nombre del modelo relacionado, nombre del campo que va a estar relacionado en el otro modelo)
    #en ese caso, "dispositivos" debe definirse en el modelo Tenant
    tenant = relationship("Tenant", back_populates="imagen")
    dispositivo = relationship("Dispositivos", back_populates="imagen")
