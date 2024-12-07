from DAOs.dao import DAO
from entidade.assoc_carro_inspecao import AssocCarroInspecao

class AssocCarroInspecaoDAO(DAO):
    def __init__(self):
        super().__init__('inspecoes.pkl')

    def add(self, assoc):
        if((assoc is not None) and isinstance(assoc, AssocCarroInspecao) and isinstance(assoc.id, int)):
            super().add(assoc.id, assoc)

    def update(self, assoc):
        if((assoc is not None) and isinstance(assoc, AssocCarroInspecao) and isinstance(assoc.id, int)):
            super().update(assoc.id, assoc)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)