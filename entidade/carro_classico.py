from carro import Carro
from motor import Motor
from roda import Roda
from pintura import Pintura

class CarroClassico(Carro):
    def __init__(self, vin: str, placa: str, modelo: str, ano: int, quilometragem: float, motor: Motor, roda: Roda, pintura: Pintura, cambio: str, unidades_existentes: int, preco_compra: float, preco_venda: float):
        
        super().__init__(vin, placa, modelo, ano, quilometragem, motor, roda, pintura, cambio)
        
        if not isinstance(unidades_existentes, int):
            raise TypeError("Unidades existentes deve ser um número inteiro")
        if not isinstance(preco_compra, float):
            raise TypeError("O preço de compra deve ser um número decimal")
        if not isinstance(preco_venda, float):
            raise TypeError("O preço de venda deve ser um número decimal")

        self.__unidades_existentes = unidades_existentes
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda

    @property
    def unidades_existentes(self) -> int:
        return self.__unidades_existentes

    @unidades_existentes.setter
    def unidades_existentes(self, unidades_existentes: int):
        if not isinstance(unidades_existentes, int):
            raise TypeError("Unidades existentes deve ser um número inteiro")
        self.__unidades_existentes = unidades_existentes

    @property
    def preco_compra(self) -> float:
        return self.__preco_compra

    @preco_compra.setter
    def preco_compra(self, preco_compra: float):
        if not isinstance(preco_compra, float):
            raise TypeError("O preço de compra deve ser um número decimal")
        self.__preco_compra = preco_compra

    @property
    def preco_venda(self) -> float:
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, preco_venda: float):
        if not isinstance(preco_venda, float):
            raise TypeError("O preço de venda deve ser um número decimal")
        self.__preco_venda = preco_venda