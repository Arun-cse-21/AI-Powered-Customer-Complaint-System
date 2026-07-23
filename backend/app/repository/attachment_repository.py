from uuid import UUID

from sqlalchemy.orm import Session

from app.models.attachment import Attachment


class AttachmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, attachment: Attachment):
        self.db.add(attachment)
        self.db.commit()
        self.db.refresh(attachment)
        return attachment

    def get_by_complaint(self, complaint_id: UUID):
        return (
            self.db.query(Attachment)
            .filter(Attachment.complaint_id == complaint_id)
            .all()
        )

    def get_by_id(self, attachment_id: UUID):
        return (
            self.db.query(Attachment)
            .filter(Attachment.id == attachment_id)
            .first()
        )