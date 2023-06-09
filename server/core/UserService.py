from domain.repository.UserRepository import UserRepository
from domain.repository.RelationshipRepository import RelationshipRepository
from domain.entity.models import User
import uuid
from passlib.hash import sha256_crypt

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_account(self, username: str, password: str, description: str):
        user_uuid = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        username_found = self.user_repo.get_by_username(username)
        if username_found:
            return False
        user = User(uuid, username, password_hash, description, 0)
        
        self.user_repo.add(user)
        return True
        
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
        