from DAOs.dao import DAO
from entidade.transferencia import Transferencia

class TransferenciaDAO(DAO):
    def __init__(self):
        super().__init__('transferencias.pkl')

    def add(self, transferencia):
        if((transferencia is not None) and isinstance(transferencia, Transferencia) and isinstance(transferencia.id, int)):
            super().add(transferencia.id, transferencia)

    def update(self, transferencia):
        if((transferencia is not None) and isinstance(transferencia, Transferencia) and isinstance(transferencia.id, int)):
            super().update(transferencia.id, transferencia)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)