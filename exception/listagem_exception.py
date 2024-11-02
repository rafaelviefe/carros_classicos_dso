class ListagemException(Exception):
    def __init__(self, message="Nenhum item encontrado na listagem."):
        super().__init__(message)