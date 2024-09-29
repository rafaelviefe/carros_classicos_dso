from motor import Motor
from roda import Roda
from pintura import Pintura

class Carro:
    def __init__(self, vin: str, placa: str, modelo: str, ano: int, quilometragem: float, motor: Motor, roda: Roda, pintura: Pintura, cambio: str):
        if not isinstance(vin, str):
            raise TypeError("O VIN deve ser uma string")
        if not isinstance(placa, str):
            raise TypeError("A placa deve ser uma string")
        if not isinstance(modelo, str):
            raise TypeError("O modelo deve ser uma string")
        if not isinstance(ano, int):
            raise TypeError("O ano deve ser um número inteiro")
        if not isinstance(quilometragem, float):
            raise TypeError("A quilometragem deve ser um número decimal")
        if not isinstance(motor, Motor):
            raise TypeError("O motor deve ser uma instância da classe Motor")
        if not isinstance(roda, Roda):
            raise TypeError("A roda deve ser uma instância da classe Roda")
        if not isinstance(pintura, Pintura):
            raise TypeError("A pintura deve ser uma instância da classe Pintura")
        if not isinstance(cambio, str):
            raise TypeError("O câmbio deve ser uma string")
        
        self.__vin = vin
        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano
        self.__quilometragem = quilometragem
        self.__motor = motor
        self.__roda = roda
        self.__pintura = pintura
        self.__cambio = cambio

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

    @property
    def quilometragem(self) -> float:
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, quilometragem: float):
        if not isinstance(quilometragem, float):
            raise TypeError("A quilometragem deve ser um número decimal")
        self.__quilometragem = quilometragem

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor: Motor):
        if not isinstance(motor, Motor):
            raise TypeError("O motor deve ser uma instância da classe Motor")
        self.__motor = motor

    @property
    def roda(self):
        return self.__roda

    @roda.setter
    def roda(self, roda: Roda):
        if not isinstance(roda, Roda):
            raise TypeError("A roda deve ser uma instância da classe Roda")
        self.__roda = roda

    @property
    def pintura(self):
        return self.__pintura

    @pintura.setter
    def pintura(self, pintura: Pintura):
        if not isinstance(pintura, Pintura):
            raise TypeError("A pintura deve ser uma instância da classe Pintura")
        self.__pintura = pintura

    @property
    def cambio(self) -> str:
        return self.__cambio