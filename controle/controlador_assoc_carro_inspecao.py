from entidade.assoc_carro_inspecao import AssocCarroInspecao
from limite.tela_assoc_carro_inpecao import TelaAssocCarroInspecao

class ControladorAssocCarroInspecao:
    def __init__(self, controlador_sistema):
        self.__associacoes = []
        self.__tela_associacao = TelaAssocCarroInspecao()
        self.__controlador_sistema = controlador_sistema
        self.__id_inspecao = 0
    
    def inclui_inspecao(self, vin = None, carro = None):
        if not vin or not carro:
            dados_carro = self.valida_vin()
            vin, carro = dados_carro[0], dados_carro[1]

        inspecoes_anteriores = self.obtem_status_inspecao(vin)
        avaliavel, cont_inapto = inspecoes_anteriores[0], inspecoes_anteriores[1]
        if not avaliavel:
            self.__tela_associacao.mostra_mensagem("ATENCAO: Este carro foi reprovado e não pode mais ser inspecionado!")
            return False
        
        apto, resultado = self.verifica_inspecao(carro, cont_inapto)
        id = self.gera_id()
        inspecao = AssocCarroInspecao(carro, id, apto, resultado)
        self.__associacoes.append(inspecao)

        return apto

    def verifica_inspecao(self, carro, cont_inapto):
                
        pecas_atuais = self.obtem_pecas_carro(carro)
        pecas_esperadas = self.__tela_associacao.pega_pecas_esperadas()

        inspecao = self.compara_pecas(pecas_atuais, pecas_esperadas)
        apto, pecas_diferentes = inspecao[0], inspecao[1]

        resultado = "aprovado" if apto else "reprovado" if (cont_inapto + 1) >= 3 else "pendente"
        self.__tela_associacao.mostra_inconstancias(pecas_diferentes)
        self.__tela_associacao.mostra_mensagem(f'Resultado da inspeção: {resultado.upper()}.')

        return apto, resultado

    def obtem_pecas_carro(self, carro):
        return {
            "num_motor": carro.motor.num_motor,
            "num_serie": carro.roda.num_serie,
            "codigo_cor": carro.pintura.codigo_cor
        }

    def busca_inspecoes_por_vin(self, vin):
        inspecoes_encontradas = []

        for associacao in self.__associacoes:
            if associacao.carro.documento.vin == vin:
                inspecoes_encontradas.append(associacao)
        return inspecoes_encontradas
        
    def obtem_status_inspecao(self, vin):
        cont_inapto = 0
        inspecoes_encontradas = self.busca_inspecoes_por_vin(vin)[:-3]

        for assoc in inspecoes_encontradas:
            if not assoc.inspecao.apto:
                cont_inapto += 1
            else:
                cont_inapto = 0
                
            if (assoc.inspecao.resultado == "reprovado") or (cont_inapto >= 3):
                return [False, cont_inapto]

        return [True, cont_inapto]

    def compara_pecas(self, pecas_atuais: dict, pecas_esperadas: dict): 
        pecas = ["motor", "roda", "pintura"]
        pecas_diferentes = {}
        condizente = True

        for peca in pecas:
            if not (pecas_atuais[peca]  == pecas_esperadas[peca]):
                pecas_diferentes = {peca: (pecas_atuais[peca], pecas_esperadas[peca])} 
                condizente = False 

        return [condizente, pecas_diferentes]

    def lista_inspecoes(self):
        vin = self.__tela_associacao.valida_vin()[0]
        inspecoes = self.busca_inspecoes_por_vin(vin)
        for inspecao in inspecoes:
            self.__tela_associacao.mostra_inspecao(inspecao)  
        return inspecoes

    def exclui_inspecao(self):
        inspecoes = self.lista_inspecoes()
        id_selecionado = self.__tela_associacao.pega_id()

        for inspecao in inspecoes:
            if inspecao.id == id_selecionado:
                self.__associacoes.remove(inspecao)    
    
    def valida_vin(self):
        vin = self.__tela_associacao.pega_vin()
        carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(vin)
        while not carro:          
            vin = self.__tela_associacao.pega_vin()
            carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(vin)
        return [vin, carro]

    def gera_id(self):
        self.__id_inspecao += 1
        return self.__id_inspecao

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_inspecao, 2: self.lista_inspecoes, 3: self.exclui_inspecao, 0: self.__controlador_sistema.abre_tela}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_peca.tela_opcoes()]()