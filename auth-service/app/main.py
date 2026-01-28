from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Auth Service activo"}
