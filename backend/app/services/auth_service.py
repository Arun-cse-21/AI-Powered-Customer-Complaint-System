from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token

from app.repository.user_repository import UserRepository


class AuthService:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def login(
        self,
        email: str,
        password: str
    ):

        user = self.repository.get_by_email(email)

        if not user:

            return None

        if not verify_password(
            password,
            user.password_hash
        ):

            return None

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role.value
            }
        )

        return token