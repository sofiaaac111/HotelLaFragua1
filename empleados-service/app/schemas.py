from pydantic import BaseModel

class EmpleadoBase(BaseModel):
    nombre: str
    cargo: str
    correo: str
    telefono: str
    estado: str = "activo"

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoResponse(EmpleadoBase):
    id: int

    class Config:
        from_attributes = True
