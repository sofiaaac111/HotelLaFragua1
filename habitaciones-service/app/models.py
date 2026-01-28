from sqlalchemy import Column, Integer, String, DECIMAL, Text, CheckConstraint
from app.database import Base

class Habitacion(Base):
    __tablename__ = "habitaciones"

    id = Column(Integer, primary_key=True, index=True)

    # CAMBIADO: numero → nombre
    nombre = Column(String(100), unique=True, nullable=False)

    tipo = Column(String(50), nullable=False)
    precio = Column(DECIMAL(10,2), nullable=False)

    estado = Column(String(20), nullable=False, default="disponible")
    descripcion = Column(Text)

    # Validación a nivel BD
    __table_args__ = (
        CheckConstraint("precio >= 0", name="precio_no_negativo"),
        CheckConstraint("estado IN ('disponible','ocupada','mantenimiento')", name="estado_valido"),
        CheckConstraint("tipo IN ('sencilla','doble','suite')", name="tipo_valido"),
    )
