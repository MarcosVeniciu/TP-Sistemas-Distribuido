import sqlite3 
import queries

class DataBase:
    def __init__(self, database="./database.db"):
        self._database = database
        self._connection = None
        
    
    def start_connection(self):
            self._connection = sqlite3.connect(self._database)
            cursor = self._connection.cursor()
            
            return cursor
    
    def commit_operation(self):
        self._connection.commit()
    
    def finish_connection(self):
        try:
            self._connection.close()
        except sqlite3.Error:
            print("")
            
    def init_db(self):
        self.connection = self.start_connection()
        self.connection.execute(queries.CREATE_TABLE_USER)
        self.connection.execute(queries.CREATE_TABLE_RECIPES)
        self.connection.execute(queries.CREATE_TABLE_RELATIONSHIP)
        self.commit_operation()
        self.finish_connection()
        
if __name__ == "__main__":
    db = DataBase()
    db.init_db()