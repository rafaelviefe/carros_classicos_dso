from carro_classico import CarroClassico
from inspecao import Inspecao

class AssocCarroInspecao:
    def __init__(self, id: int, carro: CarroClassico, inspecao: Inspecao):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de CarroClassico")
        if not isinstance(inspecao, Inspecao):
            raise TypeError("A inspecao deve ser uma instância de Inspecao")

        self.__id = id
        self.__carro = carro
        self.__inspecao = inspecao

    @property
    def id(self) -> int:
        return self.__id

    @property
    def carro(self) -> CarroClassico:
        return self.__carro

    @carro.setter
    def carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de CarroClassico")
        self.__carro = carro

    @property
    def inspecao(self) -> Inspecao:
        return self.__inspecao

    @inspecao.setter
    def inspecao(self, inspecao: Inspecao):
        if not isinstance(inspecao, Inspecao):
            raise TypeError("A inspecao deve ser uma instância de Inspecao")
        self.__inspecao = inspecao
