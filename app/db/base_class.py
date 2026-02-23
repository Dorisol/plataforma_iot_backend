"""
EL NOMNRE DE LA TABLA EN LA BD VA A SER EL NOMBRE DEL MODELO EN MINUSCULAS
"""

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    

