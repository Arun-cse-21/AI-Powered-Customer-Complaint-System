import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base
from app.models.enums import UserRole


class User(Base):

    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    role = Column(
        Enum(UserRole),
        nullable=False,
        #default=UserRole.QA_EXECUTIVE
    )

    is_active = Column(
        Boolean,
        default=True
    )

    last_login = Column(
        DateTime
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