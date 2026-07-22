from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine
from app.api.auth import router as auth_router

import app.models

app = FastAPI(
    title="AI Complaint Management System"
)

# Uncomment ONLY if you are not using Alembic yet
# Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }