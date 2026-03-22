from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.controllers.authController import login
from app.schemas.AuthSchema import LoginSchema

#endpoints

router = APIRouter()

@router.post("/auth/login", status_code=status.HTTP_200_OK)
def login_endpoint(credentials: LoginSchema, db: Session = Depends(get_db)):
    return login(db, credentials)
