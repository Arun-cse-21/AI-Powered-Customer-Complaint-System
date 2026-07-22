from app.auth.hashing import hash_password

from app.models.user import User
from app.repository.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def register(
        self,
        full_name: str,
        email: str,
        password: str,
        role
    ):

        existing = self.repository.get_by_email(email)

        if existing:
            return None

        user = User(
            full_name=full_name,
            email=email,
            password_hash=hash_password(password),
            role=role
        )

        return self.repository.create(user)