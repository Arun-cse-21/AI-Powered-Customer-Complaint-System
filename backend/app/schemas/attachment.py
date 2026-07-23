from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AttachmentResponse(BaseModel):
    id: UUID
    complaint_id: UUID
    file_name: str
    file_type: str | None
    file_size: int | None
    storage_path: str
    extracted_text: str | None
    uploaded_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True