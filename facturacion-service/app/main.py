from fastapi import FastAPI
from app.database import engine, Base
from app.routers import facturas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Facturacion Service")

app.include_router(facturas.router)

@app.get("/")
def root():
    return {"message": "Facturacion Service activo"}
