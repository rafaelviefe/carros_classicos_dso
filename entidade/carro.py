from entidade.documentacao import Documentacao
from entidade.motor import Motor
from entidade.roda import Roda
from entidade.pintura import Pintura

class Carro:
    def __init__(self, vin: str, placa: str, modelo: str, ano: int, quilometragem: float, motor: Motor, roda: Roda, pintura: Pintura, cambio: str):
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

        self.__documentacao = Documentacao(vin, placa, modelo, ano)
        self.__quilometragem = quilometragem
        self.__motor = motor
        self.__roda = roda
        self.__pintura = pintura
        self.__cambio = cambio

    @property
    def documentacao(self) -> Documentacao:
        return self.__documentacao

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
