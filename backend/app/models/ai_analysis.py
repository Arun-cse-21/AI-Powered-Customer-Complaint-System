import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class AIAnalysis(Base):

    __tablename__ = "ai_analysis"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    complaint_id = Column(
        UUID(as_uuid=True),
        ForeignKey("complaints.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    summary = Column(Text)

    risk = Column(String(50))

    risk_reason = Column(Text)

    missing_information = Column(JSONB)

    duplicate_score = Column(Float)

    duplicate_complaint_id = Column(
        UUID(as_uuid=True),
        nullable=True
    )

    root_cause = Column(JSONB)

    capa = Column(JSONB)

    llm_model = Column(String(100))

    processing_time = Column(Float)

    raw_response = Column(JSONB)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    complaint = relationship(
        "Complaint",
        back_populates="ai_analysis"
    )