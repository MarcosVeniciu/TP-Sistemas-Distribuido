from sqlalchemy.sql.expression import func, select
from sqlalchemy.orm import Session
from ..entity import models


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_username(self, username: str) -> models.User:
        stmt = select(models.User).where(models.User.username == username)
        return self.session.execute(stmt).first()