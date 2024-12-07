from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante
from entidade.carro_classico import CarroClassico

class Transferencia:
    def __init__(self, id: int, ref_pessoa, ref_carro: CarroClassico, tipo: str, valor: float):
        if not isinstance(id, int):
            raise TypeError("O ID deve ser um número inteiro")
        if not isinstance(ref_pessoa, (PessoaJuridica, Negociante)):
            raise TypeError("O documento da pessoa deve ser uma instância de Pessoa")
        if not isinstance(ref_carro, CarroClassico):
            raise TypeError("O VIN do carro deve ser uma instância de Carro Clássico")
        if tipo not in ("compra", "venda"):
            raise ValueError("O tipo de transferência deve ser 'compra' ou 'venda'")
        if not isinstance(valor, (float, int)) or valor <= 0:
            raise ValueError("O valor deve ser um número positivo")

        self.__id = id
        self.__ref_pessoa = ref_pessoa
        self.__ref_carro = ref_carro
        self.__tipo = tipo
        self.__valor = float(valor)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def ref_pessoa(self) -> str:
        return self.__ref_pessoa

    @ref_pessoa.setter
    def ref_pessoa(self, ref_pessoa):
        if not isinstance(ref_pessoa, (PessoaJuridica, Negociante)):
            raise TypeError("O ref_pessoa deve ser uma instância de Pessoa")
        self.__ref_pessoa = ref_pessoa

    @property
    def ref_carro(self) -> str:
        return self.__ref_carro

    @ref_carro.setter
    def ref_carro(self, ref_carro: CarroClassico):
        if not isinstance(ref_carro, CarroClassico):
            raise TypeError("O ref_carro deve ser uma instância de Carro Clássico")
        self._ref_carro = ref_carro

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
