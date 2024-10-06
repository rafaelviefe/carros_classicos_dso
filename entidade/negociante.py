from typing import List
from carro_classico import CarroClassico
from pessoa import Pessoa

class Negociante(Pessoa):
    def __init__(self, nome: str, documento: str, carros: List[CarroClassico] = None):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if carros is None:
            carros = []
        elif not all(isinstance(carro, CarroClassico) for carro in carros):
            raise TypeError("Todos os carros devem ser instâncias da classe Carro")
        if not isinstance(documento, str):
            raise TypeError("O CPF deve ser uma string")

        self.__nome = nome
        self.__carros = carros
        self.__documento = documento

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

    @property
    def documento(self) -> str:
        return self.__documento

    @documento.setter
    def documento(self, documento: str):
        if not isinstance(documento, str):
            raise TypeError("O CPF deve ser uma string")
        self.__documento = documento

    # função tratamento CPF