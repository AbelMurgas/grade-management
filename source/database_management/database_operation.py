import sqlite3
from decouple import config
import os
class Database:
    __DB_LOCATION = config('DB_LOCATION')
    def __init__(self):
        if os.path.isfile(Database.__DB_LOCATION):
            self.connection = self.connect()
            self.cursor = self.connection.cursor()
        else:
            raise FileNotFoundError(f"the dir {Database.__DB_LOCATION} no exist or not found")
        
    def connect(self):
        try:
            con = sqlite3.connect(Database.__DB_LOCATION)
            print("----successful connection----")
            return con
        except Exception as e:
            print(e)
    
    def close(self):
        self.connection.close()
        
    def commit(self):
        self.connection.commit()
        
    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
        

    def execute_get_one(self, query):
        self.cursor.execute(query)
        try:
            password = self.cursor.fetchone()[0]
            return password
        except:
            return None


    

    
