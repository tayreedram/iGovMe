from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="iGovMe API", version="0.1.0")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")

engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "iGovMe API is running"}

@app.get("/health/db")
def health_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT PostGIS_Version();"))
        version = result.scalar()

    return {
        "database": "ok",
        "postgis_version": version
    }