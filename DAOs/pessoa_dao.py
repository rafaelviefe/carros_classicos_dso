from DAOs.dao import DAO
from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoas.pkl')

    def add(self, pessoa):
        if((pessoa is not None) and isinstance(pessoa, (PessoaJuridica, Negociante)) and isinstance(pessoa.documento, str)):
            super().add(pessoa.documento, pessoa)

    def update(self, pessoa):
        if((pessoa is not None) and isinstance(pessoa, (PessoaJuridica, Negociante)) and isinstance(pessoa.documento, str)):
            super().update(pessoa.documento, pessoa)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)