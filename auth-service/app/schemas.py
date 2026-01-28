from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    correo: str
    password: str
    rol: str

class UsuarioLogin(BaseModel):
    correo: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    correo: str
    rol: str

    class Config:
        from_attributes = True
