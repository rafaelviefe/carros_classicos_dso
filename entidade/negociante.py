from entidade.pessoa import Pessoa

class Negociante(Pessoa):
    def __init__(self, nome: str, documento: str):
        super().__init__(nome, documento)

    def tipo(self) -> str:
        return "Negociante"