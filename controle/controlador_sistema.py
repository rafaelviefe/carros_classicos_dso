from limite.tela_sistema import TelaSistema
from controle.controlador_pessoas import ControladorPessoas
from controle.controlador_carros_classicos import ControladorCarrosClassicos
from controle.controlador_pecas import ControladorPecas

class ControladorSistema:

    def __init__(self):
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__controlador_carros_classicos = ControladorCarrosClassicos(self)
        self.__controlador_pecas = ControladorPecas(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    @property
    def controlador_carros_classicos(self):
        return self.__controlador_carros_classicos

    @property
    def controlador_pecas(self):
        return self.__controlador_pecas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastro_pessoas(self):
        self.__controlador_pessoas.abre_tela()

    def cadastro_carros(self):
        self.__controlador_carros_classicos.abre_tela()

    def cadastro_carros(self):
        self.__controlador_pecas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastro_pessoas, 2: self.cadastro_carros, 3: self.cadastro_inspecoes, 4: self.cadastro_pecas, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()