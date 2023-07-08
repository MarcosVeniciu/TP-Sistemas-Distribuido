from repository import RelationshipRepository, UserRepository, RecipeRepository
from models import Relationship, User, Recipe
import uuid
from passlib.hash import sha256_crypt
from datetime import datetime

class RelationshipService:
    def __init__(self):
        pass

    def add(self, username_1: str, username_2: str):
        user_repository         = UserRepository()
        relationship_repository = RelationshipRepository()
        
        follow_relationship_id   = uuid.uuid4()
        
        followed_user_exist = user_repository.find_user_by_username(username_1)
        follower_user_exist = user_repository.find_user_by_username(username_2)
    

        if (followed_user_exist and follower_user_exist):
            followed_user_id = followed_user_exist[0]
            follower_user_id = follower_user_exist[0]
        
            follow_relationship = Relationship(str(follow_relationship_id), followed_user_id, follower_user_id)
            response = relationship_repository.create(follow_relationship)
            
            return response
        else:
            return False
        
    def user_follows(self, username):
        answer: list = []
     
        user_repo = UserRepository()
        relation_repo = RelationshipRepository()
        
        usr = user_repo.find_user_by_username(username)
        #print(usr)
        friends = relation_repo.find(usr[0])
        #print(friends)
        for friend in friends:
            answer.append(friend[4])
        print(answer)
        return answer
        
        
class UserService:
    def __init__(self):
        pass

    def create_account(self, username: str, password: str, description: str):
        user_repo        = UserRepository()
        user_uuid = uuid.uuid4()
        password_hash = sha256_crypt.hash(password)
        username_found = user_repo.find_user_by_username(username)
        if username_found:
            return False
        user = User(uuid, username, password_hash, description)
        
        return user_repo.create(user)

        
    def login(self, username: str, password: str):
        user_repo = UserRepository()
        row = user_repo.find_user_by_username(username)

        if row is None:
            return False

        if row[2] == password:
            return True
        else:
            return False
    
    def user_description(self, username):
        user_repo = UserRepository()
        usr = user_repo.find_user_by_username(username)
        return usr[3]

    
class RecipeService:
    def __init__(self) -> None:
        pass
    
    def add(self, username, title, recipe):
        user_repository = UserRepository()
        recipe_repository = RecipeRepository()
        
        user = user_repository.find_user_by_username(username)

        if user:
            recipe_uuid = str(uuid.uuid4())
            user_uuid = user[0]
            recipe = Recipe(recipe_uuid, user_uuid, title, recipe, 0, datetime.now()) 
            
            return recipe_repository.create(recipe)
        else:
            return False
    
    def get_recipe_by_user(self, username):
        user_repository = UserRepository()
        recipe_repository = RecipeRepository()
        
        user_uuid = user_repository.find_user_by_username(username)[0]
        return recipe_repository.find_by_user_uuid(user_uuid)
    
    def get_recipe_by_title(self, title):
        recipe_repo = RecipeRepository()
        receita = recipe_repo.find_by_name(title)
        return receita
    
    def like_recipe(self, title):
        recipe_repo = RecipeRepository()
        return recipe_repo.like_recipe(title)
        