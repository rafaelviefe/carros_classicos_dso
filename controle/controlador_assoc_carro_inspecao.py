from entidade.assoc_carro_inspecao import AssocCarroInspecao
from limite.tela_assoc_carro_inpecao import TelaAssocCarroInspecao

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException

class ControladorAssocCarroInspecao:
    def __init__(self, controlador_sistema):
        self.__associacoes = []
        self.__registros = []
        self.__tela_associacao = TelaAssocCarroInspecao()
        self.__controlador_sistema = controlador_sistema
        self.__id_inspecao = 0

    # Inclui uma nova inspeção para um carro, verificando a elegibilidade do veículo e calculando o resultado da inspeção.
    def inclui_inspecao(self, vin=None, carro=None):
        self.__tela_associacao.mostra_mensagem("\nINICIANDO INSPEÇÃO...")

        try:
            if not vin or not carro:
                dados_carro = self.valida_vin()
                vin, carro = dados_carro[0], dados_carro[1]
        
            avaliavel, cont_inapto = self.obtem_status_inspecao(vin)
            if not avaliavel:
                raise InclusaoException("ATENÇÃO: Este carro foi reprovado e não pode mais ser inspecionado!")
            
            apto, resultado = self.verifica_inspecao(carro, cont_inapto)
            id = self.gera_id()
            
            try:
                inspecao = AssocCarroInspecao(carro, id, apto, resultado)
                self.__associacoes.append(inspecao)
                return apto
            except (TypeError, ValueError) as e:
                self.__tela_associacao.mostra_mensagem(f"Erro ao criar inspeção: {str(e)}")
                return False

        except InclusaoException as e:
            self.__tela_associacao.mostra_mensagem(str(e))
            return False

    # Compara as peças atuais do carro com as peças esperadas e define o resultado da inspeção.
    def verifica_inspecao(self, carro, cont_inapto):
        pecas_atuais = self.obtem_pecas_carro(carro)
        pecas_esperadas = self.__tela_associacao.pega_pecas_esperadas()

        inspecao = self.compara_pecas(pecas_atuais, pecas_esperadas)
        apto, pecas_diferentes = inspecao[0], inspecao[1]

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

        for peca in pecas:
            if pecas_atuais[peca] != pecas_esperadas[peca]:
                pecas_diferentes[peca] = (pecas_atuais[peca], pecas_esperadas[peca])
                condizente = False 

        return [condizente, pecas_diferentes]
    
    # Lista todas as inspeções de um veículo específico, buscando pelo VIN.
    def lista_inspecoes(self):
        vin = self.valida_vin()[0]
        try:
            
            inspecoes = self.busca_inspecoes_por_vin(vin)
            if not inspecoes:
                raise ListagemException(f"Nenhuma inspeção encontrada para o VIN {vin}.")
            
            for inspecao in inspecoes:
                self.__tela_associacao.mostra_inspecao(inspecao)  
            return inspecoes
        
        except ListagemException as e:
            self.__tela_associacao.mostra_mensagem(str(e))

    # Exclui uma inspeção específica após listar e selecionar pelo ID.
    def exclui_inspecao(self):
        try:
            inspecoes = self.lista_inspecoes()
            if not inspecoes:
                return

            id_selecionado = self.__tela_associacao.pega_id()
            for inspecao in inspecoes:
                if inspecao.id == id_selecionado:
                    self.__associacoes.remove(inspecao)
                    self.__tela_associacao.mostra_mensagem("Inspeção excluída com sucesso!")
                    return

            raise ExclusaoException("Inspeção com o ID fornecido não encontrada.")
        
        except ListagemException as e:
            self.__tela_associacao.mostra_mensagem(str(e))
        
        except ExclusaoException as e:
            self.__tela_associacao.mostra_mensagem(str(e))

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
    
    def inclui_registro(self):
        data = self.__tela_associacao.obtem_data()

        # Verifica se já existe um registro para essa data e o exclui, se necessário
        registro_existente = next((registro for registro in self.__registros if registro["data"] == data), None)
        if registro_existente:
            self.__registros.remove(registro_existente)
            self.__tela_associacao.mostra_mensagem(f"Atualizando registro para a data: {data}.")

        carros_registrados = []
        
        for assoc in self.__associacoes:
            carro_registrado = self.gera_registro_carro(assoc, data, carros_registrados)
            if carro_registrado:
                carros_registrados.append(carro_registrado)

        registro = {
            "data": data,
            "carros": carros_registrados
        }

        if not registro["carros"]:
            self.__tela_associacao.mostra_mensagem("Nenhuma inspeção foi encontrada neste período...")
            return

        self.__registros.append(registro)
        self.__tela_associacao.mostra_registro(registro)

    def gera_registro_carro(self, assoc, data, carros_registrados):
        carro = assoc.carro
        vin = carro.documentacao.vin

        vin_registrado = sum(1 for carro in carros_registrados if carro["vin"] == vin)
        if not vin_registrado:
            
            inspecoes_mes = [
                inspecao for inspecao in self.busca_inspecoes_por_vin(vin)
                if inspecao.data == data
            ]

            if inspecoes_mes:
                inspecoes_aprovadas = sum(1 for assoc in inspecoes_mes if assoc.inspecao.apto)
                inspecoes_pendentes = sum(1 for assoc in inspecoes_mes if assoc.inspecao.resultado == "pendente")
                inspecoes_reprovadas = len(inspecoes_mes) - inspecoes_aprovadas - inspecoes_pendentes
                ultimo_status = inspecoes_mes[-1].inspecao.resultado

                return {
                    "vin": vin,
                    "inspecoes_aprovadas": inspecoes_aprovadas,
                    "inspecoes_pendentes": inspecoes_pendentes,
                    "inspecoes_reprovadas": inspecoes_reprovadas,
                    "ultimo_status": ultimo_status
                }
        return None

    def exclui_registro(self):
        self.lista_registros()
        data = self.__tela_associacao.obtem_data()

        # Busca o registro pela data fornecida e remove, se encontrado
        for registro in self.__registros:
            if registro["data"] == data:
                self.__registros.remove(registro)
                self.__tela_associacao.mostra_mensagem("Registro excluído com sucesso!")
                return

        self.__tela_associacao.mostra_mensagem("Nenhum registro encontrado para a data especificada.")

    def altera_registro(self):
        self.lista_registros()
        self.__tela_associacao.mostra_mensagem("Precisamos da data do registro que deseja alterar.")
        data_atual = self.__tela_associacao.obtem_data()

        registro_existente = next((registro for registro in self.__registros if registro["data"] == data_atual), None)
        if not registro_existente:
            self.__tela_associacao.mostra_mensagem("Nenhum registro encontrado para a data especificada.")
            return

        self.__tela_associacao.mostra_mensagem("Precisamos da nova data do registro.")
        nova_data = self.__tela_associacao.obtem_data()

        self.__registros.remove(registro_existente)
        carros_registrados = []

        for assoc in self.__associacoes:
            carro_registrado = self.gera_registro_carro(assoc, nova_data, carros_registrados)
            if carro_registrado:
                carros_registrados.append(carro_registrado)

        novo_registro = {
            "data": nova_data,
            "carros": carros_registrados
        }

        if not novo_registro["carros"]:
            self.__tela_associacao.mostra_mensagem("Nenhuma inspeção encontrada neste período...")
            return

        self.__registros.append(novo_registro)
        self.__tela_associacao.mostra_mensagem(f"Registro atualizado para a nova data: {nova_data}.")
        self.__tela_associacao.mostra_registro(novo_registro)

    def lista_registros(self):
        
        if not self.__registros:
            self.__tela_associacao.mostra_mensagem("Nenhum registro foi encontrado.")
            return
        
        for registro in self.__registros:
            self.__tela_associacao.mostra_registro(registro) 


    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_inspecao,
            2: self.lista_inspecoes,
            3: self.exclui_inspecao,

            4: self.inclui_registro,
            5: self.exclui_registro,
            7: self.lista_registros,
            0: self.__controlador_sistema.abre_tela
        }
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_associacao.tela_opcoes()]()