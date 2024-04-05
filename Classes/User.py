from classes.gclass import Gclass

class User(Gclass):
    def __init__(self, id, nome, email, telemovel):
        super().__init__()
        self._id = int(id)
        self._nome = nome
        self._email = email
        self._telemovel = telemovel
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo):
        self._id = novo 
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo):
        self._nome = novo 
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo):
        self._email = novo 
    
    @property
    def telemovel(self):
        return self._telemovel
    
    @telemovel.setter
    def telemovel(self, novo):
        self._telemovel = novo 