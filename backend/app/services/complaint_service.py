from uuid import uuid4

from app.models.complaint import Complaint
from app.models.enums import ComplaintStatus, Priority
from app.repository.complaint_repository import ComplaintRepository


class ComplaintService:

    def __init__(self, repository: ComplaintRepository):
        self.repository = repository

    def create_complaint(self, request, current_user):

        complaint = Complaint(
    complaint_number=f"CMP-{str(uuid4())[:8]}",
    customer_name=request.customer_name,
    complaint_source=request.complaint_source,
    product_id=request.product_id,
    batch_number=request.batch_number,
    manufacturing_date=request.manufacturing_date,
    expiry_date=request.expiry_date,
    quantity_affected=request.quantity_affected,
    complaint_type=request.complaint_type,
    description=request.description,
    complaint_date=request.complaint_date,
    severity=request.severity,
    priority=Priority.MEDIUM,
    status=ComplaintStatus.DRAFT,
    created_by=current_user.id
)

        return self.repository.create(complaint)

    def get_all_complaints(self):
        return self.repository.get_all()

    def get_complaint(self, complaint_id):
        return self.repository.get_by_id(complaint_id)

    def delete_complaint(self, complaint):
        self.repository.delete(complaint)