# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:58:56 2024

@author: carva
"""
import datetime
from classes.gclass import Gclass
from classes.User import User

class Agendamentos(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_user_code','_data']
    # Class header title
    header = 'Agendamentos'
    # field description for use in, for example, in input form
    des = ['Código','Nome',"Data"]
    # Constructor: Called when an object is instantiated
    def __init__(self,code,user_code,data):
        super().__init__()
        #if code =='None':
            #codes= Agendamentos.getalist('_code')
            #if codes ==[]:
                #code = str(1)
            #else:
                #code=str(max(map(int,Agendamentos.getalist('_code')))+1)
        #if user_code in User.lst:
        # Object attributes
        self._code = code
        self._user_code = user_code
        self._data=datetime.date.fromisoformat(data)
        #else:
            #print('User', user_code, ' not found')
        

        # Add the new object to the User_login list
        Agendamentos.obj[code] = self
        Agendamentos.lst.append(code)

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, novo):
        self._code = novo 
        
    @property 
    def data(self):
        return self._data
    @data.setter 
    def data(self,novo):
        self._data=novo
    
    @property
    def user_code(self):
        return self._user_code
    
    @user_code.setter
    def user_code(self, novo):
        if novo in User.lst:
            self._user_code = novo 
        else:
            print('User', novo, ' not found')
    
    
    
    
        
