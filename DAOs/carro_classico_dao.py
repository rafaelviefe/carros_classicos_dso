from DAOs.dao import DAO
from entidade.carro_classico import CarroClassico

class CarroClassicoDAO(DAO):
    def __init__(self):
        super().__init__('carros.pkl')

    def add(self, carro):
        if((carro is not None) and isinstance(carro, CarroClassico) and isinstance(carro.documentacao.vin, str)):
            super().add(carro.documentacao.vin, carro)

    def update(self, carro):
        if((carro is not None) and isinstance(carro, CarroClassico) and isinstance(carro.documentacao.vin, str)):
            super().update(carro.documentacao.vin, carro)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)