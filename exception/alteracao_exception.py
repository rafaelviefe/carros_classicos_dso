class AlteracaoException(Exception):
    def __init__(self, message="Erro ao alterar item."):
        super().__init__(message)