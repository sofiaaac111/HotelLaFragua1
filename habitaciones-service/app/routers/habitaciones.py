from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import Habitacion

router = APIRouter()

class EstadoHabitacion(BaseModel):
    estado: str


@router.put("/habitaciones/{id}/estado")
def actualizar_estado_habitacion(
    id: int,
    data: EstadoHabitacion,
    db: Session = Depends(get_db)
):
    habitacion = db.query(Habitacion).filter(Habitacion.id == id).first()

    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")

    habitacion.estado = data.estado
    db.commit()

    return {"message": f"Habitación actualizada a {data.estado}"}
