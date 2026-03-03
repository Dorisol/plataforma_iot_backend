from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from fastapi import HTTPException, status
from app.core.config import settings
from app.schemas.AuthSchema import LoginSchema
from app.schemas.UserSchema import UserSchema
from sqlalchemy.orm import Session
from app.models.UserModel import Users
import uuid

def verificarPassword(password_plana: str, password_hasheada: str) -> bool:
    if not password_hasheada:
        return False
    return bcrypt.checkpw(
        password_plana.encode('utf-8'), 
        password_hasheada.encode('utf-8')
    )

def obtenerPassHasheada(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def crearAccesoToken(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def login(db: Session, usuarioLogin: LoginSchema):
    #Buscar el usuario en la base de datos
    user = db.query(Users).filter(Users.username == usuarioLogin.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    
    #Comparar la contraseña plana con el hash de la BD usando la función de verificación
    if not verificarPassword(usuarioLogin.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales inválidas"
        )

    #Generar token con JWT
    expiracion_token = timedelta(minutes=settings.EXPIRACION_TOKEN)
    token = crearAccesoToken(
        data={"user": user.username, "id": str(user.id_user), "tenant": str(user.fk_tenant_id)}, 
        expires_delta=expiracion_token
    )
    
    return {"access_token": token, "token_type": "bearer"}

def crearUsuario(db: Session, user_data: UserSchema):
    hashed_password = obtenerPassHasheada(user_data.password_hash)

    db_user = Users(
        id_user=uuid.uuid4(),
        fk_tenant_id=user_data.fk_tenant_id,
        username=user_data.username,
        password_hash=hashed_password,
        api_key=user_data.api_key,
        role=user_data.role,
        is_active=user_data.is_active,
        created_at=datetime.now(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
