from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    numero_documento: str
    telefono: str

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None

    class Config:
        from_attributes = True
