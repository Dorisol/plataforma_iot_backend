from sqlalchemy.orm import Session
from app.models.UsuariosModel import Usuarios
from app.schemas.UsuarioSchema import UsuarioCreate
import bcrypt

def get_usuarios(db: Session):
    return db.query(Usuarios).all()


#Desencripta la contraseña 
def obtenerPassHasheada(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')


def crearUsuario(db: Session, nuevoUsuario: UsuarioCreate):
    try:
        hashed_password = obtenerPassHasheada(nuevoUsuario.password)

        db_user = Usuarios(
            idTenant=nuevoUsuario.idTenant,
            username=nuevoUsuario.username,
            password=hashed_password,
            rol=nuevoUsuario.rol,
            isActivo=nuevoUsuario.isActivo,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    except Exception as e:
        print("Error al crear el usuario: ", e)
        return None


#eliminar usuario
def eliminarUsuario(db: Session, idUsuario: str):
    try:
        usuario = db.query(Usuarios).filter(Usuarios.idUsuario == idUsuario).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return True
    except Exception as e:
        print("Error al eliminar el usuario", e)
        return None