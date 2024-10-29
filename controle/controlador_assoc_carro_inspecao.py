from entidade.assoc_carro_inspecao import AssocCarroInspecao
from controle.controlador_carros_classicos import ControladorCarrosClassicos
from limite.tela_assoc_carro_inpecao import TelaAssocCarroInspecao

class ControladorAssocCarroInspecao:
    def __init__(self, controlador_sistema):
        self.__carros = []
        self.__associacoes = []
        self.__tela_associacao = TelaAssocCarroInspecao
        self.__controlador_sistema = controlador_sistema
        self.__assoc_carro_inspecao = AssocCarroInspecao
        self.__id_inspecao = 1

    @property
    def lista_carros(self):
        self.__carros = ControladorCarrosClassicos.carros
        return self.__carros
    
    def inclui_inspecao(self):
        vin = TelaAssocCarroInspecao.pegar_vin()
        avaliavel, cont_inapto = self.verificar_inspecoes_por_vin(vin)
        if not avaliavel:
            return #tratar retorno
        carro = ControladorCarrosClassicos.pega_carro_por_vin(vin)
        pecas_carro = self.pega_dados_carro(carro)
        pecas_carro_classico = TelaAssocCarroInspecao.pegar_dados_carro_classico()
        if not (self.comparar_pecas(pecas_carro, pecas_carro_classico)):
            apto = False
            if (cont_inapto +1) >= 3:
                resultado = "reprovado"
            else:
                resultado = "pendente"
        else:
            apto = True
            resultado = "aprovado"
        id = self.gerar_id()
        inspecao = AssocCarroInspecao(carro, id, apto, resultado)
        self.__associacoes.append(inspecao)

    def pega_dados_carro(self, carro):
        return{
            "num_motor": carro.num_motor,
            "num_serie": carro.num_serie,
            "codigo_cor": carro.codigo_cor
        }

    def buscar_inspecoes_por_vin(self, vin):
        inspecoes_encontradas = []

        for associacao in self.__associacoes:
            if associacao.carro.documento.vin == vin:
                inspecoes_encontradas.append(associacao)
        return inspecoes_encontradas
        
        
    def verificar_inspecoes_por_vin(self, vin):
        cont_inapto = 0
        inspecoes_encontradas = self.busca_inspecoes_por_vin(vin)

        for inspecao in inspecoes_encontradas:
            if (inspecao.resultado == "reprovado") or (cont_inapto>= 3):
                return False
            
            elif inspecao.resultado == "aprovado":
                return True
            
            elif inspecao.apto == False:
                cont_inapto += 1 
        return True, cont_inapto

    def gerar_id(self):
        self.__id_inspecao += 1
        return  self.__id_inspecao

    def comparar_pecas(self, pecas_carro: list, pecas_carro_classico: list): 
        pecas = ["motor", "roda", "pintura"]
        pecas_diferentes = {}

        for peca in pecas:
            if not (pecas_carro[peca]  == pecas_carro_classico[peca]):
                pecas_diferentes = {peca: (pecas_carro[peca], pecas_carro_classico[peca])}  

        return pecas_diferentes

    def lista_inspecoes(self):
        vin = TelaAssocCarroInspecao.pegar_vin()
        inspecoes = self.buscar_inspecoes_por_vin(vin)
        for inspecao in inspecoes:
            TelaAssocCarroInspecao.mostra_inspecao(inspecao)  
        return inspecoes

    def exclui_inspecao(self):
        inspecoes = self.lista_inspecoes()
        id_para_remover = TelaAssocCarroInspecao.pegar_id()

        for inspecao in inspecoes:
            if inspecao.id == id_para_remover:
                self.__associacoes.remove(inspecao)    
        return




    def abre_tela(self):
        lista_opcoes = {1: self.inclui_inspecao, 2: self.lista_inspecoes, 3: self.exclui_inspecao, 0: self.__controlador_sistema.abre_tela}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_peca.tela_opcoes()]()