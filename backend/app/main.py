from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine
from app.api.auth import router as auth_router
from app.api.complaints import router as complaint_router
from app.api.auth import router as auth_router
from app.api.complaints import router as complaint_router
from app.api.products import router as product_router
from app.api.attachments import router as attachment_router

import app.models

app = FastAPI(
    title="AI Complaint Management System"
)

# Uncomment ONLY if you are not using Alembic yet
# Base.metadata.create_all(bind=engine)
app.include_router(product_router)
app.include_router(auth_router)
app.include_router(complaint_router)
app.include_router(auth_router)
app.include_router(attachment_router)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }