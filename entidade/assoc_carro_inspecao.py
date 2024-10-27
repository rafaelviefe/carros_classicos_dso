from entidade.carro_classico import CarroClassico
from entidade.inspecao import Inspecao

class AssocCarroInspecao:
    def __init__(self, carro: CarroClassico, id: int, apto: bool, resultado: str):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de CarroClassico")
        self.__id = id
        self.__inspecao = self.Inspecao(id, apto, resultado)
        self.__carro = carro

    @property
    def id(self) -> int:
        return self.__id

    @property
    def carro(self) -> CarroClassico:
        return self.__carro

    @property
    def inspecao(self) -> Inspecao:
        return self.__inspecao