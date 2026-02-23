from sqlalchemy import Column, ForeignKey, Uuid, String, Float, Boolean, TIMESTAMP, JSON, DateTime
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Mediciones(Base):
    __tablename__ = "mediciones"
    id_medida = Column(Uuid, primary_key=True, index=True)
    fk_tenant_id = Column(Uuid, ForeignKey("tenants.id_tenant"))
    fk_user_id = Column(Uuid, ForeignKey("users.id_user"))
    variable = Column(String)
    val = Column(Float)
    unit = Column(String)
    recorded_at = Column(DateTime, default=datetime.now)
    metadata_medicion = Column("metadata",JSON)


    tenant_med = relationship("Tenant", back_populates="medicion")
    user_med = relationship("Users", back_populates="medicion")