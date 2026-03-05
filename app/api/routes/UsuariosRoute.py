from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.controllers import UsuariosController
from app.schemas import UsuarioSchema
from uuid import UUID

#endpoints
router = APIRouter()

@router.get("/usuarios/todosUsuarios", response_model=List[UsuarioSchema.UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    return UsuariosController.get_usuarios(db)


