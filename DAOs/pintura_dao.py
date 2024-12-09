from DAOs.dao import DAO
from entidade.pintura import Pintura

class PinturaDAO(DAO):
    def __init__(self):
        super().__init__('pinturas.pkl')

    def add(self, pintura):
        if((pintura is not None) and isinstance(pintura, Pintura) and isinstance(pintura.codigo_cor, str)):
            super().add(pintura.codigo_cor, pintura)

    def update(self, pintura):
        if((pintura is not None) and isinstance(pintura, Pintura) and isinstance(pintura.codigo_cor, str)):
            super().update(pintura.codigo_cor, pintura)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)