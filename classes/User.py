# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:58:56 2024

@author: carva
"""

from classes.gclass import Gclass

class User(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_nome','_email','_telemovel']
    # Class header title
    header = 'Utilizador'
    # field description for use in, for example, in input form
    des = ['Código','Nome',"E-mail","Telémovel"]
    # Constructor: Called when an object is instantiated
    def __init__(self,code,nome,email,telemovel):
        super().__init__()
        # Object attributes
        self._code = int(code)
        self._nome = nome
        self._email = email
        self._telemovel = telemovel

        # Add the new object to the User_login list
        User.obj[code] = self
        User.lst.append(code)

    
    @property
    def code(self):
        return self._id
    
    @code.setter
    def code(self, novo):
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

        
