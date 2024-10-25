from entidade.carro_classico import CarroClassico

class AssocCarroInspecao:

    class Inspecao:
        def __init__(self, id: int, apto: bool, resultado: str):
            if not isinstance(id, int):
                raise TypeError("O carro deve ser uma instância de CarroClassico")
            if not isinstance(apto, bool):
                raise TypeError("O atributo 'apto' deve ser um valor booleano")
            if not isinstance(resultado, str):
                raise TypeError("O resultado deve ser uma string")

            self.__id = id
            self.__apto = apto
            self.__resultado = resultado
            
        @property
        def id(self) -> int:
            return self.__id
        
        @property
        def resultado(self) -> str:
            return self.__resultado
        
        @property
        def apto(self) -> str:
            return self.__apto




    def __init__(self, carro: CarroClassico, id: int, apto: bool, resultado: str):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de CarroClassico")
        if not isinstance(apto, bool):
            raise TypeError("O apto deve ser uma instância de bool")
        if not isinstance(resultado, str):
            raise TypeError("O resultado deve ser uma instância de string")
        
        self.__inspecao = self.Inspecao(id, apto, resultado)
        self.__carro = carro

    @property
    def carro(self) -> CarroClassico:
        return self.__carro

    @property
    def inspecao(self) -> Inspecao:
        return self.__inspecao