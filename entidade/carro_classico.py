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
        self.__precos_compra = []
        self.__precos_venda = []

    @property
    def unidades_existentes(self) -> int:
        return self.__unidades_existentes

    @unidades_existentes.setter
    def unidades_existentes(self, unidades_existentes: int):
        if not isinstance(unidades_existentes, int):
            raise TypeError("Unidades existentes deve ser um número inteiro")
        self.__unidades_existentes = unidades_existentes

    def add_preco_compra(self, preco: float):
        if not isinstance(preco, float):
            raise TypeError("O preço de compra deve ser um número decimal")
        self.__precos_compra.append(preco)

    def del_preco_compra(self, preco: float):
        if preco in self.__precos_compra:
            self.__precos_compra.remove(preco)

    @property
    def precos_compra(self) -> list:
        return self.__precos_compra

    def add_preco_venda(self, preco: float):
        if not isinstance(preco, float):
            raise TypeError("O preço de venda deve ser um número decimal")
        self.__precos_venda.append(preco)

    def del_preco_venda(self, preco: float):
        if preco in self.__precos_venda:
            self.__precos_venda.remove(preco)

    @property
    def precos_venda(self) -> list:
        return self.__precos_venda
