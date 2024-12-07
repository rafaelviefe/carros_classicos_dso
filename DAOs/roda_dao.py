from DAOs.dao import DAO
from entidade.roda import Roda

class RodaDAO(DAO):
    def __init__(self):
        super().__init__('rodas.pkl')

    def add(self, roda):
        if((roda is not None) and isinstance(roda, Roda) and isinstance(roda.num_serie, str)):
            super().add(roda.num_serie, roda)

    def update(self, roda):
        if((roda is not None) and isinstance(roda, Roda) and isinstance(roda.num_serie, str)):
            super().update(roda.num_serie, roda)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)