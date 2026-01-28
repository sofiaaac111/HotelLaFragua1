from sqlalchemy.orm import Session
from . import models, schemas


def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

from app import models

def crear_cliente(db, cliente, user):
    nuevo = models.Cliente(
        usuario_id=user["sub"],
        correo=user["correo"],
        nombre=cliente.nombre,
        apellido=cliente.apellido,
        tipo_documento=cliente.tipo_documento,
        numero_documento=cliente.numero_documento,
        telefono=cliente.telefono
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def delete_cliente(db: Session, cliente_id: int):
    cliente = get_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente

def update_cliente(db: Session, cliente_id: int, cliente_update: schemas.ClienteUpdate):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente:
        return None

    # Solo actualiza campos enviados
    update_data = cliente_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente, key, value)

    db.commit()
    db.refresh(cliente)
    return cliente
