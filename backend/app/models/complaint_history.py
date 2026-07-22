import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.models.enums import ComplaintStatus


class ComplaintHistory(Base):

    __tablename__ = "complaint_history"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    complaint_id = Column(
        UUID(as_uuid=True),
        ForeignKey("complaints.id", ondelete="CASCADE"),
        nullable=False
    )

    old_status = Column(
        Enum(ComplaintStatus)
    )

    new_status = Column(
        Enum(ComplaintStatus)
    )

    remarks = Column(
        Text
    )

    changed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    complaint = relationship(
        "Complaint",
        back_populates="history"
    )

    user = relationship("User")