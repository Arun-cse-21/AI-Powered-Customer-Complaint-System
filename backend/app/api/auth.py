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
from app.auth.permissions import require_roles
from app.services.user_service import UserService
from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    repository = UserRepository(db)

    service = AuthService(repository)

    token = service.login(
        form_data.username,
        form_data.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return LoginResponse(
        access_token=token
    )
@router.get("/me")
def get_logged_in_user(current_user=Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role.value
    }

@router.get("/admin")
def admin_dashboard(
    current_user=Depends(require_roles("ADMIN"))
):
    return {
        "message": "Welcome Admin!"
    }