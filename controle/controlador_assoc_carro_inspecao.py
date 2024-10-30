from entidade.assoc_carro_inspecao import AssocCarroInspecao
from limite.tela_assoc_carro_inpecao import TelaAssocCarroInspecao

class ControladorAssocCarroInspecao:
    def __init__(self, controlador_sistema):
        self.__associacoes = []
        self.__tela_associacao = TelaAssocCarroInspecao()
        self.__controlador_sistema = controlador_sistema
        self.__id_inspecao = 0
    
    # Inclui uma nova inspeção para um carro, verificando a elegibilidade do veículo e calculando o resultado da inspeção.
    def inclui_inspecao(self, vin=None, carro=None):
        self.__tela_associacao.mostra_mensagem("\nINICIANDO INSPEÇÃO...")

        # Valida VIN e obtém o carro, se não fornecido
        if not vin or not carro:
            dados_carro = self.valida_vin()
            vin, carro = dados_carro[0], dados_carro[1]

        # Verifica se o carro pode ser inspecionado com base em inspeções anteriores
        inspecoes_anteriores = self.obtem_status_inspecao(vin)
        avaliavel, cont_inapto = inspecoes_anteriores[0], inspecoes_anteriores[1]
        if not avaliavel:
            self.__tela_associacao.mostra_mensagem("ATENCAO: Este carro foi reprovado e não pode mais ser inspecionado!")
            return False
        
        # Verifica se o carro passa na inspeção e cria a associação
        apto, resultado = self.verifica_inspecao(carro, cont_inapto)
        id = self.gera_id()
        inspecao = AssocCarroInspecao(carro, id, apto, resultado)
        self.__associacoes.append(inspecao)

        return apto

    # Compara as peças atuais do carro com as peças esperadas e define o resultado da inspeção.
    def verifica_inspecao(self, carro, cont_inapto):
        pecas_atuais = self.obtem_pecas_carro(carro)
        pecas_esperadas = self.__tela_associacao.pega_pecas_esperadas()

        # Compara peças e obtém peças discrepantes
        inspecao = self.compara_pecas(pecas_atuais, pecas_esperadas)
        apto, pecas_diferentes = inspecao[0], inspecao[1]

        # Define o resultado com base na aptidão e contagem de inspeções reprovadas
        if apto:
            resultado = "aprovado"
        else:
            resultado = "reprovado" if (cont_inapto + 1) >= 3 else "pendente"
        
        self.__tela_associacao.mostra_inconstancias(pecas_diferentes)
        self.__tela_associacao.mostra_mensagem(f'Resultado da inspeção: {resultado.upper()}.')

        return apto, resultado

    # Extrai as informações das peças do carro para inspeção.
    def obtem_pecas_carro(self, carro):
        return {
            "motor": carro.motor.num_motor,
            "roda": carro.roda.num_serie,
            "pintura": carro.pintura.codigo_cor
        }
    
    # Retorna uma lista de inspeções associadas ao VIN fornecido.
    def busca_inspecoes_por_vin(self, vin):
        return [assoc for assoc in self.__associacoes if assoc.carro.documentacao.vin == vin]
 
     # Verifica o status de elegibilidade de inspeções anteriores de um veículo, permitindo ou não uma nova inspeção.
    def obtem_status_inspecao(self, vin):
        cont_inapto = 0
        inspecoes_encontradas = self.busca_inspecoes_por_vin(vin)[-3:]

        for assoc in inspecoes_encontradas:
            if not assoc.inspecao.apto:
                cont_inapto += 1
            else:
                cont_inapto = 0

            if cont_inapto >= 3:
                return False, cont_inapto

        return True, cont_inapto

    # Compara as peças atuais do carro com as peças esperadas e registra discrepâncias.
    def compara_pecas(self, pecas_atuais: dict, pecas_esperadas: dict):
        pecas = ["motor", "roda", "pintura"]
        pecas_diferentes = {}
        condizente = True

        # Identifica peças que diferem das expectativas e marca inspeção como inconforme
        for peca in pecas:
            if pecas_atuais[peca] != pecas_esperadas[peca]:
                pecas_diferentes[peca] = (pecas_atuais[peca], pecas_esperadas[peca])
                condizente = False 

        return [condizente, pecas_diferentes]
    
    # Lista todas as inspeções de um veículo específico, buscando pelo VIN.
    def lista_inspecoes(self):
        vin = self.valida_vin()[0]
        inspecoes = self.busca_inspecoes_por_vin(vin)
        for inspecao in inspecoes:
            self.__tela_associacao.mostra_inspecao(inspecao)  
        return inspecoes

    # Exclui uma inspeção específica após listar e selecionar pelo ID.
    def exclui_inspecao(self):
        inspecoes = self.lista_inspecoes()
        id_selecionado = self.__tela_associacao.pega_id()

        for inspecao in inspecoes:
            if inspecao.id == id_selecionado:
                self.__associacoes.remove(inspecao)    

    # Valida a existência de um carro associado ao VIN fornecido.
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
        lista_opcoes = {
            1: self.inclui_inspecao,
            2: self.lista_inspecoes,
            3: self.exclui_inspecao,
            0: self.__controlador_sistema.abre_tela
        }
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_associacao.tela_opcoes()]()
