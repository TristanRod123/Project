from stuff.config import *
class Employer:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.__password
    
employer1 = Employer(username, password)