from abc import ABC, abstractmethod
from typing import List
from carro_classico import CarroClassico

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cnpj: str, carros: List[CarroClassico] = None):
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass
    
    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        pass
  
    @abstractmethod
    def add_carro(self, carro: CarroClassico):
        pass

    @abstractmethod
    def del_carro(self, carro: CarroClassico):
        pass
