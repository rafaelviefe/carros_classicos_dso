from entidade.assoc_carro_inspecao import AssocCarroInspecao
from controle.controlador_carros_classicos import ControladorCarrosClassicos

class ControladorAssocCarroInspecao:
    def __init__(self, controlador_sistema):
        self.__carros = []
        self.__associacoes = []
    @property
    def lista_carros(self):
        self.__carros = ControladorCarrosClassicos.carros
        return self.__carros
    
    def criar_associacao(self, carro, id, apto, resultado):
        associacao = AssocCarroInspecao(carro, id, apto, resultado)
        self.__associacoes.append(associacao)

    #ainda vou fazer o listar e excluir