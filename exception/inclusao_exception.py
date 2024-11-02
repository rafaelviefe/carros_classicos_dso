class InclusaoException(Exception):
    def __init__(self, message="Erro ao incluir item."):
        super().__init__(message)