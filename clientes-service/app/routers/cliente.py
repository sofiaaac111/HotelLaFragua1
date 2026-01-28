from fastapi import APIRouter, Depends
from app.database import get_db
from app import crud, schemas
from app.security import get_current_user, require_admin
from app import models
from sqlalchemy.orm import Session



router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/")
def crear_cliente(
    cliente: schemas.ClienteCreate,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    nuevo = models.Cliente(
        usuario_id = user["id"],          
        correo = user["correo"],          
        nombre = cliente.nombre,
        apellido = cliente.apellido,
        tipo_documento = cliente.tipo_documento,
        numero_documento = cliente.numero_documento,
        telefono = cliente.telefono
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/")
def listar_clientes(user=Depends(require_admin), db=Depends(get_db)):
    return crud.listar_clientes(db)

@router.post("/")
def crear_cliente(
    cliente: schemas.ClienteCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return crud.crear_cliente(db, cliente, user["id"])
