"""Base de Datos - Creación de Clase en ORM"""


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni= Column(Integer)
    nombre= Column(String(250))
    apellido= Column(String(250))
    
    

