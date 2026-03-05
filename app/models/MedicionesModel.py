from sqlalchemy import Column, ForeignKey, Uuid, String, Float, Boolean, TIMESTAMP, JSON, DateTime
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Mediciones(Base):
    __tablename__ = "mediciones"
    idMedicion = Column(Uuid, primary_key=True, index=True)
    idTenant = Column(Uuid, ForeignKey("tenants.idTenant"))
    idUsuario = Column(Uuid, ForeignKey("usuarios.idUsuario"))
    variable = Column(String)
    val = Column(Float)
    unit = Column(String)
    recorded_at = Column(DateTime, default=datetime.now)
    metadata_medicion = Column("metadata",JSON)


    tenant_med = relationship("Tenant", back_populates="medicion")
    usuario_med = relationship("Usuarios", back_populates="medicion")