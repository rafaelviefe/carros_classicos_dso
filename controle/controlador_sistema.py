from limite.tela_sistema import TelaSistema
from controle.controlador_pessoas import ControladorPessoas

class ControladorSistema:

    def __init__(self):
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_pessoas(self):
        self.__controlador_pessoas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_pessoas, 2: self.cadastra_carros, 3: self.cadastra_inspecoes, 4: self.cadastra_pecas, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()