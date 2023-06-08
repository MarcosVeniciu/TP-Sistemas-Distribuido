from sqlalchemy.sql.expression import func, select
from sqlalchemy.orm import Session
from ..entity import models


class RelationshipRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_uuid(self, uuid: str) -> models.Relationship:
        stmt = select(models.Relationship).where(models.Relationship.uuid == uuid)
        return self.session.execute(stmt).first()