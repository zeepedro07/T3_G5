# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:23:56 2024

@author: carva
"""
import datetime
from classes.gclass import Gclass

class Agendamentos(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    cod=0
    
    # class attributes, identifier attribute must be the first one on the list
    att = ["_code","_codeImovel","_data"]
    # Class header title
    header = 'Agendamentos'
    # field description for use in, for example, in input form
    des = ["Code","Código do Imóvel","Data (AAAA-MM-DD)"]
    # Constructor: Called when an object is instantiated
    def __init__(self,code,codeImovel, data):
        super().__init__()
        Agendamentos.cod+=1
        # Object attributes
    
        
        self._code=Agendamentos.cod
        self._codeImovel = codeImovel
        self._data=datetime.date.fromisoformat(data)

        # Add the new object to the Imovel_login list
        Agendamentos.obj[Agendamentos.cod] = self
        Agendamentos.lst.append(Agendamentos.cod)
   

        
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, novo):
        self._code = novo
        
    @property
    def codeImovel(self):
        return self._codeImovel
    
    @codeImovel.setter
    def codeImovel(self, novo):
        self._codeImovel = novo
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, novo):
        self._data = novo

    