from ast import alias
from sqlalchemy import Column, Integer, String, ForeignKey
from ..config.database import Base
from sqlalchemy.dialects.sqlite import TIMESTAMP, VARCHAR, TIME, DATE, DECIMAL, DATETIME, INTEGER

class User:
    __tablename__ = "user"
    uuid = Column(VARCHAR(100), primary_key=True)
    username = Column(VARCHAR(100))
    password = Column(VARCHAR(100))
    status = Column(INTEGER)


    def __init__(self, uuid, username, password, status) -> None:
        self.uuid = uuid
        self.username = username
        self.password = password
        self.status = status
        self.recipes = []
        self.followers = []
        self.following = []

    def as_dict(self, password=False):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        if not password:
            ret["password"] = ""

        return ret
        
class Recipe:
    __tablename__ = "recipe"
    uuid = Column(VARCHAR(100), primary_key=True)
    user_uuid = Column(VARCHAR(100), ForeignKey="user.uuid")
    ingredients = Column(VARCHAR(1000))
    preparation_mode = Column(VARCHAR(1000))
    likes = Column(INTEGER)
    created_at = Column(DATETIME)

    def __init__(self, uuid, user_uuid, ingredients, preparation_mode, likes, created_at) -> None:
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.ingredients = ingredients
        self.preparation_mode = preparation_mode
        self.likes = likes
        self.created_at = created_at
    
    def get_recipe(self):
        return self.text

class Relationship:
    __tablename__ = "relationship"
    user_uuid1 = Column(VARCHAR(100), ForeignKey="user.uuid")
    user_uuid2 = Column(VARCHAR(100), ForeignKey="user.uuid")
    