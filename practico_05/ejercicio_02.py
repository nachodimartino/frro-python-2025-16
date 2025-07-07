"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional


class DatosSocio():

    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self, dni=None, nombre=None, apellido=None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        socio = self.session.query(Socio).filter(
            Socio.id_socio == id_socio).first()

        return socio

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        socio = self.session.query(Socio).filter(
            Socio.dni == dni_socio).first()

        return socio

    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        socios = self.session.query(Socio).all()
        return socios

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        try:
            self.session.query(Socio).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        nuevo_socio = Socio(
            dni=socio.dni, nombre=socio.nombre, apellido=socio.apellido)
        self.session.add(nuevo_socio)
        self.session.commit()
        return nuevo_socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        try:
            socio = self.session.query(Socio).filter(
                Socio.id_socio == id_socio).first()
            if socio is None:
                return False

            self.session.delete(socio)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        try:
            self.session.commit()
            return socio
        except Exception:
            self.session.rollback()
            return socio  

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        from sqlalchemy import func
        return self.session.query(func.count(Socio.id_socio)).scalar() 


# NO MODIFICAR - INICIO
# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id_socio) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN
