"""
CREAR SESION DE CONEXIÓN DE BASE DE DATOS
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.core.config import settings

engine = create_engine(os.environ.get("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#autommmit --->  los cambios no se guardan automáticamente
#autoflush ---> no envía cambios automáticamente a la BD 
#bind ---> conectar la sesion al engine