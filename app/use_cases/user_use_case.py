from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, user_data: UserCreate):
        return self.user_repository.create_user(user_data)

    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.user_repository.get_users(skip, limit)
