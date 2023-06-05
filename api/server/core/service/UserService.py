from domain.repository.UserRepository import UserRepository
from domain.repository.RelationshipRepository import RelationshipRepository

class UserRepository:
    def __init__(self, user_repo: UserRepository, relation_repo: RelationshipRepository):
        self.user_repo = user_repo
        self.relation_repo = relation_repo