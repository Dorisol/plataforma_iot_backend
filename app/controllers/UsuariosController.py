from sqlalchemy.orm import Session
from app.models.UsuariosModel import Usuarios

def get_usuarios(db: Session):
    return db.query(Usuarios).all()