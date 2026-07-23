import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    product_code = Column(String(50), unique=True, nullable=False)

    product_name = Column(String(255), nullable=False)

    dosage_form = Column(String(100))

    strength = Column(String(50))

    manufacturer = Column(String(255))

    created_at = Column(DateTime(timezone=True), server_default=func.now())