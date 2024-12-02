from abc import ABC, abstractmethod
from typing import List
from entidade.carro_classico import CarroClassico

class Pessoa(ABC):
    def __init__(self, nome: str, documento: str, carros: List[CarroClassico] = None):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if not isinstance(documento, str):
            raise TypeError("O documento deve ser uma string")
        if carros is None:
            carros = []
        elif not all(isinstance(carro, CarroClassico) for carro in carros):
            raise TypeError("Todos os carros devem ser instâncias da classe CarroClassico")

        self._nome = nome
        self._documento = documento
        self._carros = carros

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        self._nome = nome

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, documento: str):
        if not isinstance(documento, str):
            raise TypeError("O documento deve ser uma string")
        self._documento = documento

    @property
    def carros(self) -> List[CarroClassico]:
        return self._carros

    def add_carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância da classe CarroClassico")
        if carro in self._carros:
            raise ValueError("O carro já está na lista")
        self._carros.append(carro)

    def del_carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância da classe CarroClassico")
        if carro not in self._carros:
            raise ValueError("O carro não está na lista")
        self._carros.remove(carro)

    @abstractmethod
    def tipo(self) -> str:
        pass