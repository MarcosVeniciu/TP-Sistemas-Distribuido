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
    
    
    def get_recipes(self, username) -> list:
        recipes = []
        try:
            for recipe in self.recipe_service.get_recipe_by_user(username):
                recipes.append(recipe[1])
            return recipes
        except:
            return recipes
    
    
    def get_recipe_by_title(self, title):
        return self.recipe_service.get_recipe_by_title(title)    
    
    
    def get_ingredients_list(self, title):
        print("here")
        recipe = self.get_recipe_by_title(title)[0]

        recipe_split = recipe[3].split("]")

        ingredients = recipe_split[0]
        ingredients = ingredients.split("|")
  
        return ingredients
    
    
    def get_preparation_mode(self, title):
        recipe = self.get_recipe_by_title(title)[0]
        recipe_split = recipe[3].split("]")
        print(recipe_split)
        return recipe_split[1]
    
    
    def get_likes(self, title):
        recipe = self.get_recipe_by_title(title)[0]
        return recipe[4]
    
    
    def get_user_description(self, username):
        return self.user_service.user_description(username)
    
    
    def follow_user(self, username, user_to_follow):
        return self.relation_service.add(username, user_to_follow)
    
    
    def add_recipe(self, username, title, ingredients, preparation_mode):
        recipe = ""
        sz = len(ingredients)
        for i in range(sz):
            if i < sz-1:
                recipe += ingredients[i] + '|'
            else:
                recipe += ingredients[i] + ']'
        recipe += preparation_mode
        
        return self.recipe_service.add(username, title, recipe)
    
    def like_recipe(self, name):
        return self.recipe_service.like_recipe(name)
    
if __name__ == '__main__':
    daemon = Pyro5.api.Daemon()


    objeto_remoto = RemoteServer()
    objeto_remoto.get_recipes("canna")
    uri = daemon.register(objeto_remoto)


    ns = Pyro5.api.locate_ns()

    ns.register("servidor", uri) 
    
    print("Servidor aguardando conexões...")
    daemon.requestLoop()


