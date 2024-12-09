from entidade.carro import Carro
from entidade.motor import Motor
from entidade.roda import Roda
from entidade.pintura import Pintura

class CarroClassico(Carro):
    def __init__(self, vin: str, placa: str, modelo: str, ano: int, quilometragem: float, motor: Motor, roda: Roda, pintura: Pintura, cambio: str, unidades_existentes: int):
        super().__init__(vin, placa, modelo, ano, quilometragem, motor, roda, pintura, cambio)

        if not isinstance(unidades_existentes, int):
            raise TypeError("Unidades existentes deve ser um número inteiro")

        self.__unidades_existentes = unidades_existentes

    @property
    def unidades_existentes(self) -> int:
        return self.__unidades_existentes

    @unidades_existentes.setter
    def unidades_existentes(self, unidades_existentes: int):
        if not isinstance(unidades_existentes, int):
            raise TypeError("Unidades existentes deve ser um número inteiro")
        self.__unidades_existentes = unidades_existentes