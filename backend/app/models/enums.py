from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    QA_MANAGER = "QA_MANAGER"
    QA_EXECUTIVE = "QA_EXECUTIVE"
    CUSTOMER = "CUSTOMER"


class ComplaintStatus(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    INVESTIGATION = "INVESTIGATION"
    CAPA = "CAPA"
    CLOSED = "CLOSED"


class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"


class Priority(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"