CREATE_USER = """ 
    INSERT INTO user (
        uuid, 
        username, 
        password, 
        description
    ) VALUES (?,?,?,?)
"""

QUERY_USER_FROM_UUID = """
    SELECT *
    FROM user
    WHERE uuid = (?)
"""

QUERY_USER_FROM_USERNAME = """
    SELECT *
    FROM user
    WHERE username = (?)
"""

CREATE_RECIPE = """
    INSERT INTO recipe (
        uuid,
        title, 
        fk_user_uuid, 
        recipe, 
        likes, 
        created_at
    ) VALUES (?,?,?,?,?,?)
"""

QUERY_RECIPE_UUID = """
    SELECT *
    FROM recipe
    WHERE
    uuid = (?)
"""

QUERY_RECIPE_NAME = """
    SELECT *
    FROM recipe
    WHERE
    title = (?)
"""

QUERY_RECIPE_USER_UUID = """
    SELECT *
    FROM recipe
    WHERE
    fk_user_uuid = (?)
"""

CREATE_TABLE_RECIPES = """
CREATE TABLE IF NOT EXISTS recipe(
    uuid VARCHAR(100) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    fk_user_uuid VARCHAR(100) NOT NULL,
    recipe VARCHAR(5000) NOT NULL,
    likes INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (fk_user_uuid) REFERENCES user (uuid)         
);
"""

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS user(
    uuid TEXT PRIMARY KEY, 
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    description TEXT NOT NULL  
);
"""
CREATE_TABLE_RELATIONSHIP = """
CREATE TABLE IF NOT EXISTS relationship(
    uuid TEXT PRIMARY KEY,
    fk_relationship_user_followed NOT NULL,
    fk_relationship_user_follower NOT NULL,
    FOREIGN KEY (fk_relationship_user_followed) REFERENCES user (uuid),
    FOREIGN KEY (fk_relationship_user_follower) REFERENCES user (uuid)
);
"""

CREATE_RELATIONSHIP = """ 
    INSERT INTO 
        relationship (uuid, fk_relationship_user_followed, fk_relationship_user_follower) 
    VALUES (?,?,?)
"""

FETCH_RELATIONSHIPS__UUID = """ 
    SELECT 
        fk_relationship_user_followed
    FROM 
        relationship 
    WHERE fk_relationship_user_follower = (?)
"""

FETCH_RELATIONSHIPS = """ 
    SELECT 
        *
    FROM 
        relationship 
    JOIN user ON relationship.fk_relationship_user_followed = user.uuid
    WHERE fk_relationship_user_follower = (?)
"""

SET_LIKE = """
    UPDATE recipe
    SET likes = likes + 1
    WHERE
        title = (?)
"""