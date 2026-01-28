from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()  # 👈 carga el .env

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB")

if not all([MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB]):
    raise ValueError("Variables de entorno MySQL no definidas")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT @@hostname, @@port, DATABASE()"))
    print("DB REAL =>", result.fetchone())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()