import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.models.enums import ComplaintStatus
from app.models.enums import Priority
from app.models.enums import Severity


class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    complaint_number = Column(
        String(30),
        unique=True,
        nullable=False
    )

    customer_name = Column(
        String(255),
        nullable=False
    )

    complaint_source = Column(
        String(100)
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False
    )

    batch_number = Column(
        String(100)
    )

    manufacturing_date = Column(
        Date
    )

    expiry_date = Column(
        Date
    )

    quantity_affected = Column(
        Integer
    )

    complaint_type = Column(
        String(100)
    )

    description = Column(
        Text,
        nullable=False
    )

    complaint_date = Column(
        Date
    )

    severity = Column(
        Enum(Severity)
    )

    priority = Column(
        Enum(Priority)
    )

    status = Column(
        Enum(ComplaintStatus),
        default=ComplaintStatus.DRAFT
    )

    assigned_to = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    created_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product = relationship("Product")

    creator = relationship(
        "User",
        foreign_keys=[created_by]
    )

    assignee = relationship(
        "User",
        foreign_keys=[assigned_to]
    )

    attachments = relationship(
        "Attachment",
        back_populates="complaint",
        cascade="all, delete-orphan"
    )

    ai_analysis = relationship(
        "AIAnalysis",
        back_populates="complaint",
        uselist=False,
        cascade="all, delete-orphan"
    )

    history = relationship(
        "ComplaintHistory",
        back_populates="complaint",
        cascade="all, delete-orphan"
    )