import Pyro5.api
from models import User, Recipe, Relationship
from service import UserService, RelationshipService, RecipeService
from repository import UserRepository, RecipeRepository, RelationshipRepository

@Pyro5.api.expose
class RemoteServer():
    def __init__(self) -> None:
        self.user_service = UserService()
        self.relation_service = RelationshipService()
        self.recipe_service = RecipeService()
        
    def login(self, username, password):
        return self.user_service.login(username, password)
    
    def get_friends(self, username):
        return self.relation_service.user_follows(username)
    
    def get_recipe(self, username):
        return self.recipe_service.get_recipe_by_user(username)
    
    def get_recipe_by_title(self, title):
        return self.recipe_service.get_recipe_by_title(title)    
    
    def get_user_description(self, username):
        return self.user_service.user_description(username)
    
    
    
if __name__ == '__main__':
    daemon = Pyro5.api.Daemon()

    # Registra o objeto remoto no servidor Pyro5
    objeto_remoto = RemoteServer()
    uri = daemon.register(objeto_remoto)

    # Obtém uma referência ao Name Server
    ns = Pyro5.api.locate_ns()

    # Registra a URI do objeto remoto no Name Server
    ns.register("servidor", uri) # registra o name server como servidor

    # Inicia o servidor Pyro5
    print("Servidor aguardando conexões...")
    daemon.requestLoop()

import Pyro5.api
from models import User, Recipe, Relationship
from service import UserService, RelationshipService, RecipeService
from repository import UserRepository, RecipeRepository, RelationshipRepository

@Pyro5.api.expose
class RemoteServer():
    def __init__(self) -> None:
        self.user_service = UserService()
        self.relation_service = RelationshipService()
        self.recipe_service = RecipeService()
        
    def login(self, username, password):
        return self.user_service.login(username, password)
    
    def get_friends(self, username):
        return self.relation_service.user_follows(username)
    
    def get_recipe(self, username):
        return self.recipe_service.get_recipe_by_user(username)
    
    def get_recipe_by_title(self, title):
        return self.recipe_service.get_recipe_by_title(title)    
    
    def get_user_description(self, username):
        return self.user_service.user_description(username)
    
    
    
if __name__ == '__main__':
    daemon = Pyro5.api.Daemon()

    # Registra o objeto remoto no servidor Pyro5
    objeto_remoto = RemoteServer()
    uri = daemon.register(objeto_remoto)

    # Obtém uma referência ao Name Server
    ns = Pyro5.api.locate_ns()

    # Registra a URI do objeto remoto no Name Server
    ns.register("servidor", uri) # registra o name server como servidor

    # Inicia o servidor Pyro5
    print("Servidor aguardando conexões...")
    daemon.requestLoop()

