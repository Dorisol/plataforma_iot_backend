from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.controllers import UsuariosController
from app.schemas import UsuarioSchema
from app.schemas.UsuarioSchema import UsuarioCreate, UsuarioBase
from uuid import UUID

#endpoints
router = APIRouter()

@router.get("/usuarios/todosUsuarios", response_model=List[UsuarioSchema.UsuarioConTenant])
def get_usuarios(db: Session = Depends(get_db)):
    return UsuariosController.get_usuarios(db)

@router.post("/usuarios/crearUsuario", response_model=UsuarioBase)
def crearUsuario(user_data: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuariosController.crearUsuario(db, user_data)

@router.delete("/usuarios/eliminarUsuario/{idUsuario}")
def eliminarUsuario(idUsuario: UUID, db: Session = Depends(get_db)):
    return UsuariosController.eliminarUsuario(db, idUsuario)

