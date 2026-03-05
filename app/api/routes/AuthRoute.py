from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.controllers.authController import login, crearUsuario
from app.schemas.AuthSchema import LoginSchema
from app.schemas.UsuarioSchema import UsuarioCreate


#endpoints

router = APIRouter()

@router.post("/auth/login", status_code=status.HTTP_200_OK)
def login_endpoint(credentials: LoginSchema, db: Session = Depends(get_db)):
    return login(db, credentials)

@router.post("/auth/registrarUsuario", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UsuarioCreate, db: Session = Depends(get_db)):
    return crearUsuario(db, user_data)