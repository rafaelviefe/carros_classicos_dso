class Documentacao:
    def __init__(self, vin: str, placa: str, modelo: str, ano: int):
        if not isinstance(vin, str):
            raise TypeError("O VIN deve ser uma string")
        if not isinstance(placa, str):
            raise TypeError("A placa deve ser uma string")
        if not isinstance(modelo, str):
            raise TypeError("O modelo deve ser uma string")
        if not isinstance(ano, int):
            raise TypeError("O ano deve ser um número inteiro")

        self.__vin = vin
        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano

    @property
    def vin(self) -> str:
        return self.__vin

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        if not isinstance(placa, str):
            raise TypeError("A placa deve ser uma string")
        self.__placa = placa

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def ano(self) -> int:
        return self.__ano
