from typing import List
from carro_classico import Carro
from pessoa import Pessoa

class Negociante(Pessoa):
    def __init__(self, nome: str, cpf: str, carros: List[Carro] = None):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if carros is None:
            carros = []
        elif not all(isinstance(carro, Carro) for carro in carros):
            raise TypeError("Todos os carros devem ser instâncias da classe Carro")
        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser uma string")

        self.__nome = nome
        self.__carros = carros
        self.__cpf = cpf

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if not isinstance(cpf, str):
            raise TypeError("O cpf deve ser uma string")
        self.__cpf = cpf