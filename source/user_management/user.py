from distutils.log import error
import bcrypt
from database_management.database_operation import Database


class User:
    def __init__(self, user: str = "", password: str = ""):
        self.id = None
        self.user = user
        self.password = password
        if user and password:
            self.login(self.user, self, password)

    def login(self, user: str, password: str) -> bool:
        check = password.encode('utf-8')
        self.password = bytes(self.__get_user_password(user).encode('utf-8'))
        if not self.password:
            print("Incorrect User")
            return False
        else:
            if bcrypt.checkpw(check, self.password):
                print("login success")
                return True
            else:
                print("incorrect password")
                return False

    def __get_user_password(self, user: str):
        conn = Database()
        query = f"""SELECT password 
            FROM student
            WHERE name_user = '{user}'"""
        password = conn.execute_get_one(query)
        return password
    
    def register(self,user:str, password: str):
        conn = Database()
        if " " in user or self.errors_in_passsword(password):
            return False
        encrypted_password = self.__encrypting_password(password)
        query = f"""INSERT INTO student (name_user,password)
        VALUES('{user}','{encrypted_password}')"""
        conn.execute_insert_one(query)
        conn.commit()
        conn.close()
        return True
        
    def errors_in_passsword(self,password:str) -> list:
        """
        1. must have at least one capital letter and one symbol
        2. range 8-12
        3. must have numbers
        
        Args:
            password (str): password that be validate

        Returns:
            list: list with errors, if not validate it will a empty lisg
        """
        errors = ['range 8-12','must have at least one capital letter','must have numbers', 'must have at least one symbol allow: $@#!-_&^* ']
        current_error = []
        symbol_allow = ['$','@','#','!','-','_','&','^','*']
        if not len(password) >= 6 or  not len(password) <= 20:
            current_error.append(errors[0])
        if not any(char.isupper() for char in password):
            current_error.append(errors[1])
        if not any(char.isdigit() for char in password):
            current_error.append(errors[2])
        if not any(char in symbol_allow for char in password):
            current_error.append(errors[3])
        return current_error
        
    def __encrypting_password(self, password:str):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)).decode('utf8')
        return hashed
