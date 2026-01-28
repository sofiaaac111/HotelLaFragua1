from sqlalchemy import Column, Integer, String
from app.database import Base
from app import schemas

class Habitacion(Base):
    __tablename__ = "habitaciones"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True)
    tipo = Column(String)
    estado = Column(String)
    descripcion = Column(String)