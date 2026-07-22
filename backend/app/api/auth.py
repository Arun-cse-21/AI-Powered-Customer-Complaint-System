from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repository.user_repository import UserRepository
from app.schemas.auth import LoginRequest
from app.schemas.auth import LoginResponse
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    request: UserCreate,
    db: Session = Depends(get_db)
):

    repository = UserRepository(db)

    service = UserService(repository)

    user = service.register(
        full_name=request.full_name,
        email=request.email,
        password=request.password,
        role=request.role
    )

    if not user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return UserResponse(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        role=user.role
    )


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    repository = UserRepository(db)

    service = AuthService(repository)

    token = service.login(
        request.email,
        request.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return LoginResponse(
        access_token=token
    )