from pydantic import BaseModel, field_validator
from typing import Literal, Optional


# -----------------------------
# Base: Campos generales
# -----------------------------
class HabitacionBase(BaseModel):
    nombre: str
    tipo: Literal["sencilla", "doble", "suite"]
    precio: float
    estado: Literal["disponible", "ocupada", "mantenimiento"]
    descripcion: Optional[str] = None

    # Validación: Precio positivo
    @field_validator("precio")
    def precio_no_negativo(cls, v):
        if v < 0:
            raise ValueError("El precio no puede ser negativo")
        return v


# -----------------------------
# Crear habitación
# -----------------------------
class HabitacionCreate(HabitacionBase):
    pass


# -----------------------------
# Actualizar habitación
# -----------------------------
class HabitacionUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[Literal["sencilla", "doble", "suite"]] = None
    precio: Optional[float] = None
    estado: Optional[Literal["disponible", "ocupada", "mantenimiento"]] = None
    descripcion: Optional[str] = None

    @field_validator("precio")
    def precio_no_negativo(cls, v):
        if v is not None and v < 0:
            raise ValueError("El precio no puede ser negativo")
        return v


# -----------------------------
# Respuesta al cliente
# -----------------------------
class Habitacion(HabitacionBase):
    id: int

    model_config = {
        "from_attributes": True  # reemplaza orm_mode=True en Pydantic v2
    }


class HabitacionResponse(HabitacionBase):
    id: int

    class Config:
        orm_mode = True