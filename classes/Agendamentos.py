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
    

    att = ["_code","_codeImovel","_data"]

    header = 'Agendamentos'

    des = ["Code","Código do Imóvel","Data (AAAA-MM-DD)"]

    def __init__(self,code,codeImovel, data):
        super().__init__()
        Agendamentos.cod+=1

        if self._is_duplicate(codeImovel, data):
            raise ValueError("Appointment already exists for the given property and date.")
        
        self._code=Agendamentos.cod
        self._codeImovel = codeImovel
        self._data=datetime.date.fromisoformat(data)


        Agendamentos.obj[Agendamentos.cod] = self
        Agendamentos.lst.append(Agendamentos.cod)
        
    def _is_duplicate(self, codeImovel, data):
        for obj in Agendamentos.obj.values():
            if obj.codeImovel == codeImovel and obj.data == datetime.date.fromisoformat(data):
                return True
        return False
   

        
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

    
