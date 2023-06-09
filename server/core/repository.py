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
                    str(recipe.ingredients),
                    str(recipe.preparation_mode),
                    str(recipe.likes),
                    str(recipe.created_at)
                ]
            )
            
            connection.commit_operation()
            connection.finish_connection()
            
        except SQL.OperationalError:
            cursor.execute(queries.CREATE_TABLE_RECIPES)
            connection.commit_operation()
            cursor.execute(queries.CREATE_RECIPE, 
                [
                    str(recipe.uuid), 
                    str(recipe.title), 
                    str(recipe.user_uuid), 
                    str(recipe.ingredients),
                    str(recipe.preparation_mode),
                    str(recipe.likes),
                    str(recipe.created_at)
                ]
            )
            connection.commit_operation()
            connection.finish_connection()
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
            cursor.execute(queries.CREATE_TABLE_USER)
            connection.commit_operation()
            cursor.execute(queries.CREATE_USER, 
                [
                    str(user.uuid), 
                    str(user.username),
                    str(user.password),
                    str(user.description)
                ]
            )
            connection.commit_operation()
            connection.finish_connection()
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
            cursor.execute(queries.CREATE_TABLE_RELATIONSHIP)
            connection.commit_operation()
            cursor.execute(queries.CREATE_RELATIONSHIP, 
                [
                    str(relationship.uuid), 
                    str(relationship.user_uuid1),
                    str(relationship.user_uuid2)
                ]
            )
            connection.commit_operation()
            connection.finish_connection()
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
    user = User("b", "canna", "0x3f3f3f3f3f3f3f", "Cozinheiro há quatro anos. Trabalho num restaurante renomado.")
    user2 = User("a", "bis", "666", "Cozinho com tempero aromáticos, especializado na culinária italiana de Friuli-Parma.")
    user_repo = UserRepository()
    user_repo.create(user)
    user_repo.create(user2)
    print(user_repo.find_user_by_username(user.username)[0])
    print(user_repo.find_user_by_username(user2.username))
    
    recipe = Recipe("a", "b", "pao com linguica", "pao, linguiça", "prepara ai", 0, datetime.today())
    recipe_repo = RecipeRepository()
    recipe_repo.create(recipe)
    print(recipe_repo.find_by_user_uuid("b"))
    
    rel1 = Relationship("ab", user.uuid, user2.uuid)
    rel2 = Relationship("ba", user2.uuid, user.uuid)
    relation_repo = RelationshipRepository()
    relation_repo.create(rel1)
    relation_repo.create(rel2)
    print(relation_repo.find("a"))
    print(type(relation_repo.find("b")))
    
    
    