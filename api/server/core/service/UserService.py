from domain.repository.UserRepository import UserRepository
from domain.repository.RelationshipRepository import RelationshipRepository
from domain.entity.models import User

class UserService:
    def __init__(self, user_repo: UserRepository, relation_repo = RelationshipRepository):
        self.user_repo = user_repo
        self.relation_repo = relation_repo

    def login(self, username: str, password: str):
        row = self.user_repo.get_by_username(username)

        if row is None:
            return {"message": "uuid não encontrado", "status": "error"}

        user: User = row.User

        if user.password == password:
            ret = {}
            ret["user"] = user.as_dict(password=False)
            ret["message"] = "Login efetuado com sucesso"
            ret["status"] = "success"
            return ret
        else:
            return {"message": "Senha incorreta", "status": "error"}