from datetime import date
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import Severity
from app.models.enums import Priority
from app.models.enums import ComplaintStatus


class ComplaintCreate(BaseModel):
    customer_name: str
    complaint_source: str | None = None
    product_id: UUID
    batch_number: str
    manufacturing_date: date
    expiry_date: date
    quantity_affected: int | None = None
    complaint_type: str | None = None
    description: str
    complaint_date: date
    severity: Severity


class ComplaintUpdate(BaseModel):
    status: ComplaintStatus | None = None
    priority: Priority | None = None
    assigned_to: UUID | None = None


class ComplaintResponse(BaseModel):
    id: UUID
    complaint_number: str
    customer_name: str
    complaint_source: str | None
    batch_number: str
    description: str
    severity: Severity
    priority: Priority
    status: ComplaintStatus
    created_at: datetime

    class Config:
        from_attributes = True

class ComplaintAssign(BaseModel):
    assigned_to: UUID


class ComplaintStatusUpdate(BaseModel):
    status: ComplaintStatus