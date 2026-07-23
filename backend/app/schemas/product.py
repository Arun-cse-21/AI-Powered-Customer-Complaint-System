from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_code: str
    product_name: str
    dosage_form: str | None = None
    strength: str | None = None
    manufacturer: str | None = None


class ProductResponse(BaseModel):
    id: UUID
    product_code: str
    product_name: str
    dosage_form: str | None = None
    strength: str | None = None
    manufacturer: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True