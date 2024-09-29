class Roda:
    def __init__(self, num_serie: str, largura: float, perfil: float, tipo: str, diametro_aro: int, indice_carga: int, indice_velocidade: str):
        if not isinstance(num_serie, str):
            raise TypeError("O número de série deve ser uma string")
        if not isinstance(largura, float):
            raise TypeError("A largura deve ser um número decimal")
        if not isinstance(perfil, float):
            raise TypeError("O perfil deve ser um número decimal")
        if not isinstance(tipo, str):
            raise TypeError("O tipo deve ser uma string")
        if not isinstance(diametro_aro, int):
            raise TypeError("O diâmetro do aro deve ser um número inteiro")
        if not isinstance(indice_carga, int):
            raise TypeError("O índice de carga deve ser um número inteiro")
        if not isinstance(indice_velocidade, str):
            raise TypeError("O índice de velocidade deve ser uma string")

        self.__num_serie = num_serie
        self.__largura = largura
        self.__perfil = perfil
        self.__tipo = tipo
        self.__diametro_aro = diametro_aro
        self.__indice_carga = indice_carga
        self.__indice_velocidade = indice_velocidade

    @property
    def num_serie(self) -> str:
        return self.__num_serie

    @property
    def largura(self) -> float:
        return self.__largura

    @property
    def perfil(self) -> float:
        return self.__perfil

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def diametro_aro(self) -> int:
        return self.__diametro_aro

    @property
    def indice_carga(self) -> int:
        return self.__indice_carga

    @property
    def indice_velocidade(self) -> str:
        return self.__indice_velocidade
