class ExclusaoException(Exception):
    def __init__(self, message="Erro ao excluir item."):
        super().__init__(message)