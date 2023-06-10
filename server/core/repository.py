import sqlite3 as SQL

from models import Recipe, User, Relationship
from database import DataBase
import queries
import uuid
from datetime import datetime

class RecipeRepository:
    def __init__(self) -> None:
        pass
    def create(self, recipe: Recipe):
        connection = DataBase()
            
        cursor = connection.start_connection()
        try:
            cursor.execute(
                queries.CREATE_RECIPE, 
                [
                    str(recipe.uuid), 
                    str(recipe.title), 
                    str(recipe.user_uuid), 
                    str(recipe.recipe),
                    str(recipe.likes),
                    str(recipe.created_at)
                ]
            )
            
            connection.commit_operation()
            connection.finish_connection()
            
        except SQL.OperationalError:
            return False
        except SQL.IntegrityError:
            return False
        else: 
            return True

    def find_by_user_uuid(self, user_uuid):
        try:
            connection = DataBase()
            cursor = connection.start_connection()
            cursor.execute(
                queries.QUERY_RECIPE_USER_UUID, 
                [
                    str(user_uuid)
                ]
            )
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
            
        except SQL.OperationalError:
            pass
        else:
            if (len(retrived_data) == 0):
                return False
            else:
                return retrived_data
    
    def find_by_uuid(self, uuid):
        try:
            connection = DataBase()
        
            cursor = connection.start_connection()
            cursor.execute(
                queries.QUERY_RECIPE_UUID, 
                [
                    str(uuid)
                ]
            )
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
        except SQL.OperationalError:
            return False
        except SQL.IntegrityError:
            return False
        else:
            if (len(retrived_data) == 0):
                return False
            else:
                return retrived_data
    
class UserRepository:
    def __init__(self) -> None:
        pass
    
    def find_user_by_username(self, username):
        try:
            connection = DataBase()
        
            cursor = connection.start_connection()
            cursor.execute(
                queries.QUERY_USER_FROM_USERNAME, 
                [
                    str(username)
                ]
            )
            connection.commit_operation()
            
            retrived_data = cursor.fetchone()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data
    
    def create(self, user: User):
        connection = DataBase()
        
        cursor = connection.start_connection()
        try:
            cursor.execute(
                queries.CREATE_USER, 
                [
                    str(user.uuid), 
                    str(user.username), 
                    str(user.password),
                    str(user.description)
                ]
            )

            connection.commit_operation()

            connection.finish_connection()
        
        except SQL.IntegrityError:
            return False
        except SQL.OperationalError:
            return False
        else:
            return True

class RelationshipRepository:
    def __init__(self) -> None:
        pass
    
    def create(self, relationship: Relationship):
        connection = DataBase()
        cursor = connection.start_connection()
        
        try:
            cursor.execute(
                queries.CREATE_RELATIONSHIP, 
                [
                    str(relationship.uuid), 
                    str(relationship.user_uuid1),    
                    str(relationship.user_uuid2)
                ]
            )
            
            connection.commit_operation()
            connection.finish_connection()
            
        except SQL.OperationalError:
            return False
        except SQL.IntegrityError:
            return False
        else:
            return True
        
    def find(self, user_id):
        try:
            connection = DataBase()
        
            cursor = connection.start_connection()
            
            cursor.execute(
                queries.FETCH_RELATIONSHIPS, 
                [
                    str(user_id)
                ]
            )
            
            connection.commit_operation()
            
            retrived_data = cursor.fetchall()

            connection.finish_connection()
        except SQL.IntegrityError:
            return False
        else:
            return retrived_data

if __name__ == "__main__":
    user = User("a", "canna", "1234", "Cozinheiro ha quatro anos. Trabalho num restaurante renomado.")
    user2 = User("b", "bis", "666", "Cozinho com temperos aromaticos, especializado na culinaria italiana de Friuli-Parma.")
    user3 = User("c", "bolacha", "31413", "Nao eh biscoito")
    user_repo = UserRepository()
    user_repo.create(user)
    user_repo.create(user2)
    user_repo.create(user3)
    print(user_repo.find_user_by_username(user.username)[0])
    print(user_repo.find_user_by_username(user2.username))
    
    recipe = Recipe("a", "b", "pao de bataaata", "pao, batata. tudo dento", 0, datetime.today())
    recipe_repo = RecipeRepository()
    recipe_repo.create(Recipe("a", "b", "pao de bataaata", "pao, batata. tudo dento", 0, datetime.today()))
    recipe_repo.create(Recipe("b", "b", "sopa de preda", "preda, agua. tudo dento", 0, datetime.today()))
    recipe_repo.create(Recipe("c", "c", "Bacalhau a Milanesa", "2 bacalhau\n Uma milanesa\n Modo de preparo:\nTudo dento", 0, datetime.today()))
    recipe_repo.create(Recipe("d", "a", "Lambisgoia a crepioca", "alho, crepe, lambisgoia fresca", 0, datetime.today()))
    recipe_repo.create(Recipe("e", "a", "Tomate cru", "Tomate. So comer", 0, datetime.today()))
    print(recipe_repo.find_by_user_uuid("a"))
    print(recipe_repo.find_by_user_uuid("b"))
    print(recipe_repo.find_by_user_uuid("c"))
    
    rel1 = Relationship("ab", user.uuid, user2.uuid)
    rel2 = Relationship("ba", user2.uuid, user.uuid)
    rel3 = Relationship("ac", user.uuid, user3.uuid)
    rel4 = Relationship("ca", user3.uuid, user.uuid)
    
    relation_repo = RelationshipRepository()
    relation_repo.create(rel1)
    relation_repo.create(rel2)
    relation_repo.create(rel3)
    relation_repo.create(rel4)
    print(relation_repo.find("a"))
    
    # print(relation_repo.find("b"))
    # print(relation_repo.find("c"))
    
    
    