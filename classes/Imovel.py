# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:23:56 2024

@author: carva
"""

from classes.gclass import Gclass

class Imovel(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ["_endereco","_preco","_tipologia","_area_util","_n_casas_de_banho","_n_quartos,_modalidade","_piscina","_tipoimovel","_num_andar","_num_garagens","_area_exterior","_area_total"]
    # Class header title
    header = 'Imóvel'
    # field description for use in, for example, in input form
    des = ["Endereço","Preço","Tipologia","Área Util","Número de casas de banho","Número de quartos","Modalidade","Piscina","Tipo de Imóvel","Número do andar","Número de lugares de garagem","Área exterior","Área total"]
    # Constructor: Called when an object is instantiated
    def __init__(self, endereco,preco,tipologia,area_util,n_casas_de_banho,n_quartos,modalidade,piscina,tipoimovel,num_andar,num_garagens,area_exterior,area_total):
        super().__init__()
        # Object attributes
        self._endereco = endereco
        self._preco = preco
        self._tipologia = tipologia
        self._area_util = area_util
        self._n_casas_de_banho = n_casas_de_banho
        self._n_quartos = n_quartos
        self._modalidade = modalidade
        self._piscina = piscina
        self._tipoimovel = tipoimovel
        self._num_andar = num_andar
        self._num_garagens = num_garagens
        self._area_exterior = area_exterior
        self._area_total = area_total

        # Add the new object to the Imovel_login list
        Imovel.obj[endereco] = self
        Imovel.lst.append(endereco)

    
    
    @property
    def endereco(self):
        return self._endereco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def tipologia(self):
        return self._tipologia

    @tipologia.setter
    def tipologia(self, tipologia):
        self._tipologia = tipologia

    @property
    def area_util(self):
        return self._area_util

    @area_util.setter
    def area_util(self, area_util):
        self._area_util = area_util

    @property
    def n_casas_de_banho(self):
        return self._n_casas_de_banho

    @n_casas_de_banho.setter
    def n_casas_de_banho(self, n_casas_de_banho):
        self._n_casas_de_banho = n_casas_de_banho

    @property
    def n_quartos(self):
        return self._n_quartos

    @n_quartos.setter
    def n_quartos(self, n_quartos):
        self._n_quartos = n_quartos

    @property
    def modalidade(self):
        return self._modalidade

    @modalidade.setter
    def modalidade(self, modalidade):
        self._modalidade = modalidade

    @property
    def piscina(self):
        return self._piscina

    @piscina.setter
    def piscina(self, piscina):
        self._piscina = piscina

    @property
    def tipoimovel(self):
        return self._tipoimovel

    @tipoimovel.setter
    def tipoimovel(self, tipoimovel):
        self._tipoimovel = tipoimovel

    @property
    def num_andar(self):
        return self._num_andar

    @num_andar.setter
    def num_andar(self, num_andar):
        self._num_andar = num_andar

    @property
    def num_garagens(self):
        return self._num_garagens

    @num_garagens.setter
    def num_garagens(self, num_garagens):
        self._num_garagens = num_garagens

    @property
    def area_exterior(self):
        return self._area_exterior

    @area_exterior.setter
    def area_exterior(self, area_exterior):
        self._area_exterior = area_exterior

    @property
    def area_total(self):
        return self._area_total

    @area_total.setter
    def area_total(self, area_total):
        self._area_total = area_total
