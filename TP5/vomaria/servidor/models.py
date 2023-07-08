class User:
    def __init__(self, uuid, username, password, description) -> None:
        self.uuid = uuid
        self.username = username
        self.password = password
        self.description = description
        self.recipes = []
        self.followers = []
        self.following = []

class Recipe:
    def __init__(self, uuid, user_uuid, title, recipe, likes, created_at) -> None:
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.title = title
        self.recipe = recipe
        self.likes = likes
        self.created_at = created_at

class Relationship:
    def __init__(self, uuid: str,  user_uuid1: str, user_uuid2: str) -> None:
        self.uuid = uuid
        self.user_uuid1 = user_uuid1
        self.user_uuid2 = user_uuid2

    if __name__ == '__main__':
        user = User('1234', 'joao', '13', 0)