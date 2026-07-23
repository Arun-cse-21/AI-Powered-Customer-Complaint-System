from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.permissions import require_roles
from app.models.user import User
from app.schemas.attachment import AttachmentResponse
from app.services.attachment_service import AttachmentService

router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)


@router.post(
    "/{complaint_id}",
    response_model=AttachmentResponse
)
def upload_attachment(
    complaint_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles(
            "CUSTOMER",
            "QA_MANAGER",
            "QA_EXECUTIVE"
        )
    )
):

    service = AttachmentService(db)

    return service.upload(
        complaint_id,
        current_user.id,
        file
    )


@router.get(
    "/{complaint_id}",
    response_model=list[AttachmentResponse]
)
def get_attachments(
    complaint_id: UUID,
    db: Session = Depends(get_db)
):

    service = AttachmentService(db)

    return service.get_attachments(
        complaint_id
    )