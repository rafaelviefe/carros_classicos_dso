class Inspecao:
    def __init__(self, id: int, apto: bool, resultado: str):
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
    def apto(self) -> bool:
        return self.__apto