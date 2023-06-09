from repository import RelationshipRepository, UserRepository, RecipeRepository
from models import Relationship, User, Recipe
import uuid
from passlib.hash import sha256_crypt


class RelationshipService:
    def __init__(self, user_repo: RelationshipRepository):
        self.relation_repo = user_repo

    def add(self, uuid_1: str, uuid_2: str):
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        follow_relationship_id   = uuid.uuid4()
        
        followed_user_exist = user_repository.find_user_by_username(uuid_1)
        follower_user_exist = user_repository.find_user_by_username(uuid_2)
        
        followed_user_id = followed_user_exist[0]
        follower_user_id = follower_user_exist[0]
        
        follow_relationship = Relationship(
            str(follow_relationship_id), 
            followed_user_id, 
            follower_user_id,
        )

        if (followed_user_exist and follower_user_exist):
            response = relationship_repository.create(follow_relationship)
            
            return response
        else:
            return False

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_account(self, username: str, password: str, description: str):
        user_uuid = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        username_found = self.user_repo.find_user_by_username(username)
        if username_found:
            return False
        user = User(uuid, username, password_hash, description)
        
        self.user_repo.create(user)
        return True
        
    def login(self, username: str, password: str):
        row = self.user_repo.find_user_by_username(username)

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