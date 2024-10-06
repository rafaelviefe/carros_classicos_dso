class Pintura:
    def __init__(self, codigo_cor: str, cor: str, tipo: str, camadas: int):
        if not isinstance(codigo_cor, str):
            raise TypeError("O código de cor deve ser uma string")
        if not isinstance(cor, str):
            raise TypeError("A cor deve ser uma string")
        if not isinstance(tipo, str):
            raise TypeError("O tipo deve ser uma string")
        if not isinstance(camadas, int):
            raise TypeError("As camadas devem ser um número inteiro")
        
        self.__codigo_cor = codigo_cor
        self.__cor = cor
        self.__tipo = tipo
        self.__camadas = camadas

    @property
    def codigo_cor(self) -> str:
        return self.__codigo_cor
    
    @property
    def cor(self) -> str:
        return self.__cor

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def camadas(self) -> int:
        return self.__camadas