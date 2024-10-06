class Inspecao:
    def __init__(self, id: int, apto: bool, resultado: str):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(apto, bool):
            raise TypeError("O atributo 'apto' deve ser um valor booleano")
        if not isinstance(resultado, str):
            raise TypeError("O carro deve ser uma instância de CarroClassico")

        self.__id = id
        self.__apto = apto
        self.__resultado = resultado

    @property
    def id(self) -> int:
        return self.__id

    @property
    def apto(self) -> bool:
        return self.__apto

    @apto.setter
    def apto(self, apto: bool):
        if not isinstance(apto, bool):
            raise TypeError("O atributo 'apto' deve ser um valor booleano")
        self.__apto = apto

    @property
    def resultado(self) -> str:
        return self.__resultado

    @resultado.setter
    def resultado(self, resultado: str):
        if not isinstance(resultado, str):
            raise TypeError("O resultado deve ser uma string")
        self.__resultado = resultado