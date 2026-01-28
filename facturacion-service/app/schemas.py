from pydantic import BaseModel
from datetime import date

class FacturaBase(BaseModel):
    reserva_id: int
    cliente_id: int
    subtotal: float
    impuestos: float
    total: float
    metodo_pago: str
    estado: str = "pendiente"

class FacturaCreate(FacturaBase):
    pass

class FacturaResponse(FacturaBase):
    id: int
    fecha: date

    class Config:
        from_attributes = True
