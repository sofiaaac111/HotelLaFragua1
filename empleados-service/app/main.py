from fastapi import FastAPI
from app.database import engine, Base
from app.routers import empleados

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Empleados Service")

app.include_router(empleados.router)

@app.get("/")
def root():
    return {"message": "Empleados Service activo"}
