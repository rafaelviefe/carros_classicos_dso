from typing import List
from carro_classico import Carro
from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, cnpj: str, carros: List[Carro] = None):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if carros is None:
            carros = []
        elif not all(isinstance(carro, Carro) for carro in carros):
            raise TypeError("Todos os carros devem ser instâncias da classe Carro")
        if not isinstance(cnpj, str):
            raise TypeError("O CNPJ deve ser uma string")

        self.__nome = nome
        self.__carros = carros
        self.__cnpj = cnpj

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if not isinstance(cnpj, str):
            raise TypeError("O cnpj deve ser uma string")
        self.__cnpj = cnpj