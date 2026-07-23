import os
import shutil
import uuid

from fastapi import UploadFile

from app.models.attachment import Attachment
from app.repository.attachment_repository import AttachmentRepository

UPLOAD_FOLDER = "uploads/complaints"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class AttachmentService:

    def __init__(self, db):
        self.repository = AttachmentRepository(db)

    def upload(
        self,
        complaint_id,
        uploaded_by,
        file: UploadFile,
    ):

        extension = file.filename.split(".")[-1]

        filename = f"{uuid.uuid4()}.{extension}"

        storage_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        with open(storage_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_size = os.path.getsize(storage_path)

        attachment = Attachment(
            complaint_id=complaint_id,
            uploaded_by=uploaded_by,
            file_name=file.filename,
            file_type=file.content_type,
            file_size=file_size,
            storage_path=storage_path,
            extracted_text=None
        )

        return self.repository.create(attachment)

    def get_attachments(self, complaint_id):
        return self.repository.get_by_complaint(
            complaint_id
        )