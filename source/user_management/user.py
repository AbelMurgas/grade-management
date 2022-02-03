import bcrypt
from database_management.database_operation import Database


class User:
    def __init__(self, user: str = "", password: str = ""):
        self.id = None
        self.user = user
        self.password = password
        if user and password:
            self.login(self.user, self, password)

    def login(self, user: str, password: str):
        check = password.encode('utf-8')
        self.password = bytes(self.__get_user_password(user).encode('utf-8'))
        print(self.password)
        if not self.password:
            print("Incorrect User")
        else:
            if bcrypt.checkpw(check, self.password):
                print("login success")
            else:
                print("incorrect password")

    def __get_user_password(self, user: str):
        conn = Database()
        query = f"""SELECT password 
            FROM student
            WHERE name_user = '{user}'"""
        password = conn.execute_get_one(query)
        return password

    def __encrypting_password(self, password:str):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)).decode('utf8')
        return hashed
