from abc import ABC, abstractmethod
from typing import List
from carro_classico import CarroClassico

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, carros: List[CarroClassico]):
        pass

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        self.__nome = nome

    def add_carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância da classe Carro")
        if carro in self.__carros:
            raise ValueError("O carro já está na lista")
        self.__carros.append(carro)

    def del_carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância da classe Carro")
        if carro not in self.__carros:
            raise ValueError("O carro não está na lista")
        self.__carros.remove(carro)
