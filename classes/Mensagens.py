# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:23:19 2024

@author: carva
"""

from classes.gclass import Gclass

class Mensagens(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ["_code","_cdi","_cdu","_msg","_dataehora"]
    # Class header title
    header = 'Mensagens'
    # field description for use in, for example, in input form
    des = ["Code","Código Imóvel","Código Utilizador","Texto","Data e hora"]
    # Constructor: Called when an object is instantiated
    def __init__(self,code,cdi,cdu,msg,dataehora):
        super().__init__()
        # Object attributes
        self._code=code
        self._cdi = cdi
        self._cdu = cdu
        self._msg = msg
        self._dataehora = dataehora
      
        # Add the new object to the Mensagens_login list
        Mensagens.obj[code] = self
        Mensagens.lst.append(code)

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, code):
        self._code = code
        
    @property
    def cdi(self):
        return self._cdi
    
    @cdi.setter
    def cdi(self, cdi):
        self._cdi = cdi
        
    @property
    def cdu(self):
        return self._cdu
    
    @cdu.setter
    def cdu(self, cdu):
        self._cdu = cdu
        
    @property
    def msg(self):
        return self._msg
    
    @msg.setter
    def msg(self, msg):
        self._msg = msg
        
    @property
    def dataehora(self):
        return self._dataehora
    
    @dataehora.setter
    def dataehora(self, dataehora):
        self._dataehora = dataehora
    
    
