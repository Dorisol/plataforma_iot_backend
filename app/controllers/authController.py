from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from fastapi import HTTPException, status
from app.core.config import settings
from app.schemas.AuthSchema import LoginSchema
from app.schemas.UsuarioSchema import UsuarioCreate
from sqlalchemy.orm import Session
from app.models.UsuariosModel import Usuarios
import uuid

#verifica si la contraseña hasheada y la contraseña plana coinciden
def verificarPassword(password_plana: str, password_hasheada: str) -> bool:
    if not password_hasheada:
        return False
    return bcrypt.checkpw(
        password_plana.encode('utf-8'), 
        password_hasheada.encode('utf-8')
    )

#Desencripta la contraseña 
def obtenerPassHasheada(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

#Genera el JWT para poder realizar peticiones. 
def crearToken(datos: dict, expiracion: timedelta = None):
    datosCodificar = datos.copy()

    #calcular tiempo expiracion. Si hay una expiracion válida, deja ese. Sino, deja un tiempo de 15 min
    if expiracion: 
        expire = datetime.utcnow() + expiracion
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    #agregar el tiempo de expiracion a los datos    
    datosCodificar.update({"exp": expire})

    #retornar token
    jwt_token = jwt.encode(datosCodificar, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return jwt_token


def login(db: Session, usuarioLogin: LoginSchema):
    #Buscar el usuario en la base de datos
    usuario = db.query(Usuarios).filter(Usuarios.username == usuarioLogin.username).first()
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    
    #Comparar la contraseña plana con el hash de la BD usando la función de verificación
    if not verificarPassword(usuarioLogin.password, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales inválidas"
        )

    #Generar token con JWT
    expiracion_token = timedelta(minutes=settings.EXPIRACION_TOKEN)
    token = crearToken(
        datos={"usuario": usuario.username, "idUsuario": str(usuario.idUsuario), "idTenant": str(usuario.idTenant), "rol": usuario.rol}, 
        expiracion=expiracion_token
    )
    
    return {"access_token": token, "token_type": "bearer"}

def crearUsuario(db: Session, nuevoUsuario: UsuarioCreate):
    hashed_password = obtenerPassHasheada(nuevoUsuario.password)

    db_user = Usuarios(
        idUsuario=uuid.uuid4(),
        idTenant=nuevoUsuario.idTenant,
        username=nuevoUsuario.username,
        password=hashed_password,
        rol=nuevoUsuario.rol,
        isActivo=True,
        created_at=datetime.now(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
