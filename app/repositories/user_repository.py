from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate):
        db_user = UserModel(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(UserModel).offset(skip).limit(limit).all()
