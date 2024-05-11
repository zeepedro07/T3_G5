from classes.gclass import Gclass

class Imovel(Gclass):
    def __init__(self, endereco, preco, tipologia, area_util, n_casas_de_banho, n_quartos, modalidade, piscina, tipoimovel, num_andar, num_garagens, area_exterior, num_vagas, area_total):
        super().__init__()
        self.endereco = endereco
        self.preco = preco
        self.tipologia = tipologia
        self.area_util = area_util
        self.n_casas_de_banho = n_casas_de_banho
        self.n_quartos = n_quartos
        self.modalidade = modalidade
        self.piscina = piscina
        self.tipoimovel = tipoimovel
        self.num_andar = num_andar
        self.num_garagens = num_garagens
        self.area_exterior = area_exterior
        self.num_vagas = num_vagas
        self.area_total = area_total

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_preco(self, preco):
        self.preco = preco

    def set_tipologia(self, tipologia):
        self.tipologia = tipologia

    def set_area_util(self, area_util):
        self.area_util = area_util

    def set_n_casas_de_banho(self, n_casas_de_banho):
        self.n_casas_de_banho = n_casas_de_banho

    def set_n_quartos(self, n_quartos):
        self.n_quartos = n_quartos

    def set_modalidade(self, modalidade):
        self.modalidade = modalidade

    def set_piscina(self, piscina):
        self.piscina = piscina
        
    def tipoimovel(self, tipoimovel):
        self.tipoimovel = tipoimovel
        
    def num_andar(self, num_andar):
        self.num_andar = num_andar
        
    def num_garagens(self, num_garagens):
        self.num_garagens = num_garagens
        
    def area_exterior(self, area_exterior):
        self.area_exterior = area_exterior
        
    def num_vagas(self, num_vagas):
        self.num_vagas = num_vagas
        
    def area_total(self, area_total):
        self.area_total = area_total
