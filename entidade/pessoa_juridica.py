from entidade.pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, documento: str, carros=None):
        super().__init__(nome, documento, carros)

    def tipo(self) -> str:
        return "Pessoa Jurídica"