import pickle
from abc import ABC, abstractmethod

from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException
from exception.alteracao_exception import AlteracaoException

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            raise AlteracaoException("Erro ao atualizar objeto.")

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise ListagemException("Objeto não encontrado na memória.")

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise ExclusaoException("Erro ao deletar objeto.")

    def get_all(self):
        return self.__cache.values()