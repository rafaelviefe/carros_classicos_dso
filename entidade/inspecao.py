from entidade.carro_classico import CarroClassico

class Inspecao:
    def __init__(self, id: int, carro: CarroClassico, apto: bool, resultado: str):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de CarroClassico")
        if not isinstance(apto, bool):
            raise TypeError("O atributo 'apto' deve ser um valor booleano")
        if not isinstance(resultado, str):
            raise TypeError("O resultado deve ser uma string")

        self.__id = id
        self.__carro = carro
        self.__inspecao = Inspecao(id, apto, resultado)

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
    def inspecao(self, apto: bool, resultado: str):
        if not isinstance(apto, bool):
            raise TypeError("O atributo 'apto' deve ser um valor booleano")
        if not isinstance(resultado, str):
            raise TypeError("O resultado deve ser uma string")
        self.__inspecao = Inspecao(self.__id, apto, resultado)