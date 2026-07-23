from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.permissions import require_roles
from app.database.database import get_db
from app.repository.complaint_repository import ComplaintRepository
from app.services.complaint_service import ComplaintService
from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintResponse,
    ComplaintAssign,
    ComplaintStatusUpdate,
)
from app.models.user import User
router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


@router.post(
    "/",
    response_model=ComplaintResponse,
    status_code=status.HTTP_201_CREATED
)
def create_complaint(
    request: ComplaintCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("CUSTOMER"))
):
    repository = ComplaintRepository(db)
    service = ComplaintService(repository)

    return service.create_complaint(
        request,
        current_user
    )


@router.get(
    "/",
    response_model=list[ComplaintResponse]
)
def get_all_complaints(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "ADMIN",
            "QA_MANAGER",
            "QA_EXECUTIVE",
            "CUSTOMER"
        )
    )
):
    repository = ComplaintRepository(db)
    service = ComplaintService(repository)

    return service.get_all_complaints()

@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def get_complaint(
    complaint_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(
        "ADMIN",
        "QA_MANAGER",
        "QA_EXECUTIVE",
        "CUSTOMER"
    ))
):
    repository = ComplaintRepository(db)
    service = ComplaintService(repository)

    complaint = service.get_complaint(complaint_id)

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint

@router.put("/{complaint_id}/assign")
def assign_complaint(
    complaint_id: UUID,
    request: ComplaintAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("QA_MANAGER"))
):
    service = ComplaintService(db)
    return service.assign(complaint_id, request.assigned_to)

@router.put("/{complaint_id}/status")
def update_status(
    complaint_id: UUID,
    request: ComplaintStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("QA_MANAGER", "QA_EXECUTIVE"))
):
    service = ComplaintService(db)
    return service.change_status(
        complaint_id,
        request.status
    )