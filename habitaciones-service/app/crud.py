from sqlalchemy.orm import Session
from app import models, schemas


# -----------------------------
# Obtener todas las habitaciones
# -----------------------------
def get_habitaciones(db: Session):
    return db.query(models.Habitacion).all()


# -----------------------------
# Obtener una por ID
# -----------------------------
def get_habitacion(db: Session, habitacion_id: int):
    return db.query(models.Habitacion).filter(models.Habitacion.id == habitacion_id).first()


# -----------------------------
# Crear una habitación
# -----------------------------
def create_habitacion(db: Session, habitacion: schemas.HabitacionCreate):
    db_habitacion = models.Habitacion(
        nombre=habitacion.nombre,
        tipo=habitacion.tipo,
        precio=habitacion.precio,
        estado=habitacion.estado,
        descripcion=habitacion.descripcion
    )
    db.add(db_habitacion)
    db.commit()
    db.refresh(db_habitacion)
    return db_habitacion


# -----------------------------
# Actualizar una habitación
# -----------------------------
def update_habitacion(db: Session, habitacion_id: int, data: schemas.HabitacionUpdate):
    db_habitacion = get_habitacion(db, habitacion_id)
    if not db_habitacion:
        return None

    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_habitacion, key, value)

    db.commit()
    db.refresh(db_habitacion)
    return db_habitacion


# -----------------------------
# Eliminar una habitación
# -----------------------------
def delete_habitacion(db: Session, habitacion_id: int):
    db_habitacion = get_habitacion(db, habitacion_id)
    if not db_habitacion:
        return None

    db.delete(db_habitacion)
    db.commit()
    return True
