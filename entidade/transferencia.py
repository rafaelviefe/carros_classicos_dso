class Transferencia:
    def __init__(self, id: int, documento_pessoa: str, vin_carro: str, tipo: str, valor: float):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(documento_pessoa, str):
            raise TypeError("O documento da pessoa deve ser uma string")
        if not isinstance(vin_carro, str):
            raise TypeError("O VIN do carro deve ser uma string")
        if tipo not in ("compra", "venda"):
            raise ValueError("O tipo de transferência deve ser 'compra' ou 'venda'")
        if not isinstance(valor, (float, int)) or valor <= 0:
            raise ValueError("O valor deve ser um número positivo")

        self.__id = id
        self.__documento_pessoa = documento_pessoa
        self.__vin_carro = vin_carro
        self.__tipo = tipo
        self.__valor = float(valor)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def documento_pessoa(self) -> str:
        return self.__documento_pessoa

    @documento_pessoa.setter
    def documento_pessoa(self, documento_pessoa: str):
        if not isinstance(documento_pessoa, str):
            raise TypeError("O documento_pessoa deve ser uma string")
        self.__documento_pessoa = documento_pessoa

    @property
    def vin_carro(self) -> str:
        return self.__vin_carro

    @vin_carro.setter
    def vin_carro(self, vin_carro: str):
        if not isinstance(vin_carro, str):
            raise TypeError("O vin_carro deve ser uma string")
        self._vin_carro = vin_carro

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O valor deve ser uma string")
        self._valor = valor
