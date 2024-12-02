from abc import ABC, abstractmethod
from typing import List

class Pessoa(ABC):
    def __init__(self, nome: str, documento: str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        if not isinstance(documento, str):
            raise TypeError("O documento deve ser uma string")

        self.__nome = nome
        self.__documento = documento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string")
        self.__nome = nome

    @property
    def documento(self) -> str:
        return self.__documento

    @documento.setter
    def documento(self, documento: str):
        if not isinstance(documento, str):
            raise TypeError("O documento deve ser uma string")
        self.__documento = documento

    @abstractmethod
    def tipo(self) -> str:
        pass