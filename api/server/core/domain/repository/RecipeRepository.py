from sqlalchemy.sql.expression import func, select
from sqlalchemy.orm import Session
from ..entity import models


class RecipeRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_uuid(self, uuid: str) -> models.Recipe:
        stmt = select(models.Recipe).where(models.Recipe.uuid == uuid)
        return self.session.execute(stmt).first()
    
    def get_by_user(self, user_uuid: str) :
        stmt = select(models.Recipe).where(models.Recipe.user_uuid1 == user_uuid or models.Recipe.user_uuid2 == user_uuid)