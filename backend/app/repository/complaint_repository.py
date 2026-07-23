from uuid import UUID

from sqlalchemy.orm import Session

from app.models.complaint import Complaint


class ComplaintRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, complaint: Complaint):
        self.db.add(complaint)
        self.db.commit()
        self.db.refresh(complaint)
        return complaint

    def get_by_id(self, complaint_id: UUID):
        return (
            self.db.query(Complaint)
            .filter(Complaint.id == complaint_id)
            .first()
        )

    def get_all(self):
        return (
            self.db.query(Complaint)
            .order_by(Complaint.created_at.desc())
            .all()
        )

    def update(self):
        self.db.commit()

    def delete(self, complaint: Complaint):
        self.db.delete(complaint)
        self.db.commit()

    from uuid import UUID

    def assign_complaint(self, complaint_id: UUID, user_id: UUID):
        complaint = self.get_by_id(complaint_id)
        if complaint:
            complaint.assigned_to = user_id
            self.db.commit()
            self.db.refresh(complaint)
        return complaint


    def update_status(self, complaint_id: UUID, status):
        complaint = self.get_by_id(complaint_id)
        if complaint:
            complaint.status = status
            self.db.commit()
            self.db.refresh(complaint)
        return complaint