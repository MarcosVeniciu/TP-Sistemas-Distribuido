import Pyro5.api
from models import User, Recipe, Relationship
from service import UserService, RelationshipService, RecipeService
from repository import UserRepository, RecipeRepository, RelationshipRepository

@Pyro5.api.expose
class RemoteUser():
    def __init__(self) -> None:
        user_service = UserService()
        relation_repository = RelationshipService()
    
    

@Pyro5.api.expose
class RemoteRecipe():
    def __init__(self) -> None:
        recipe_repository = RecipeService()