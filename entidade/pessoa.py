from abc import ABC, abstractmethod
from typing import List
from entidade.carro_classico import CarroClassico

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, documento: str, carros: List[CarroClassico] = None):
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass
    
    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        pass

    @property
    @abstractmethod
    def carros(self) -> List[CarroClassico]:
        pass
  
    @abstractmethod
    def add_carro(self, carro: CarroClassico):
        pass

    @abstractmethod
    def del_carro(self, carro: CarroClassico):
        pass

    @property
    @abstractmethod
    def documento(self) -> str:
        pass

    @documento.setter
    @abstractmethod
    def documento(self, documento: str):
        pass