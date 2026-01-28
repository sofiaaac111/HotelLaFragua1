from pydantic import BaseModel
from datetime import date

class ReservaBase(BaseModel):
    cliente_id: int
    habitacion_id: int
    fecha_inicio: date
    fecha_fin: date
    total: float

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id: int
    estado: str

    class Config:
        from_attributes = True