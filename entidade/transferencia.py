from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante
from entidade.carro_classico import CarroClassico

class Transferencia:
    def __init__(self, id: int, pessoa, carro: CarroClassico, tipo: str, valor: float):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(pessoa, (PessoaJuridica, Negociante)):
            raise TypeError("O documento da pessoa deve ser uma instância de Pessoa")
        if not isinstance(carro, CarroClassico):
            raise TypeError("O VIN do carro deve ser uma instância de Carro Clássico")
        if tipo not in ("compra", "venda"):
            raise ValueError("O tipo de transferência deve ser 'compra' ou 'venda'")
        if not isinstance(valor, (float, int)) or valor <= 0:
            raise ValueError("O valor deve ser um número positivo")

        self.__id = id
        self.__pessoa = pessoa
        self.__carro = carro
        self.__tipo = tipo
        self.__valor = float(valor)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def pessoa(self) -> str:
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        if not isinstance(pessoa, (PessoaJuridica, Negociante)):
            raise TypeError("O pessoa deve ser uma instância de Pessoa")
        self.__pessoa = pessoa

    @property
    def carro(self) -> str:
        return self.__carro

    @carro.setter
    def carro(self, carro: CarroClassico):
        if not isinstance(carro, CarroClassico):
            raise TypeError("O carro deve ser uma instância de Carro Clássico")
        self._carro = carro

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, float):
            raise TypeError("O valor deve ser um número decimal")
        self.__valor = valor
