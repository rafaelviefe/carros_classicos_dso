from limite.tela_carro_classico import TelaCarroClassico
from entidade.carro_classico import CarroClassico

class ControladorCarrosClassicos:

    def __init__(self, controlador_sistema):
        self.__carros = []
        self.__tela_carro_classico = TelaCarroClassico()
        self.__controlador_sistema = controlador_sistema

    # Busca um carro na lista de carros pelo número VIN e o retorna.
    def pega_carro_por_vin(self, vin: str):
        for carro in self.__carros:
            if carro.documentacao.vin == vin:
                return carro
        return None

    # Obtém e valida as peças do carro; verifica a disponibilidade para evitar duplicidade entre carros.
    def obtem_e_verifica_pecas(self, carro_atual=""):
        pecas_carro = self.__tela_carro_classico.pega_pecas_carro()

        # Recupera motor, roda e pintura a partir dos números fornecidos pelo usuário.
        motor = self.__controlador_sistema.controlador_pecas.pega_motor_por_num(pecas_carro["num_motor"])
        roda = self.__controlador_sistema.controlador_pecas.pega_roda_por_num(pecas_carro["num_serie"])
        pintura = self.__controlador_sistema.controlador_pecas.pega_pintura_por_cod(pecas_carro["codigo_cor"])

        # Checa a existência de todas as peças requisitadas.
        if not motor or not roda or not pintura:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Uma ou mais peças não foram encontradas. Verifique os códigos e tente novamente.")
            return None, None, None

        # Verifica se as peças estão disponíveis (não associadas a outros carros).
        if self.verifica_disponibilidade_peca("motor", motor.num_motor, carro_atual):
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Este motor já está associado a outro carro.")
            return None, None, None
        if self.verifica_disponibilidade_peca("roda", roda.num_serie, carro_atual):
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Esta roda já está associada a outro carro.")
            return None, None, None
        if self.verifica_disponibilidade_peca("pintura", pintura.codigo_cor, carro_atual):
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Esta pintura já está associada a outro carro.")
            return None, None, None

        return motor, roda, pintura

    # Inclui um novo carro na lista após verificar as peças e obter os dados do carro.
    def inclui_carro(self):
        motor, roda, pintura = self.obtem_e_verifica_pecas()

        if not motor or not roda or not pintura:
            return

        # Coleta os dados do carro a partir da interface.
        dados_carro = self.__tela_carro_classico.pega_dados_carro()

        # Cria uma nova instância de CarroClassico e a adiciona à lista.
        carro = CarroClassico(
            vin=dados_carro["vin"],
            placa=dados_carro["placa"],
            modelo=dados_carro["modelo"],
            ano=dados_carro["ano"],
            quilometragem=dados_carro["quilometragem"],
            motor=motor,
            roda=roda,
            pintura=pintura,
            cambio=dados_carro["cambio"],
            unidades_existentes=dados_carro["unidades_existentes"]
        )

        self.__carros.append(carro)
        self.lista_carros()

    # Modifica os dados de um carro existente na lista.
    def altera_carro(self):
        self.lista_carros()
        vin_carro = self.__tela_carro_classico.seleciona_carro()
        carro = self.pega_carro_por_vin(vin_carro)

        # Atualiza os atributos do carro se ele for encontrado.
        if carro is not None:
            novos_dados_carro = self.__tela_carro_classico.pega_alteracoes_carro()
            carro.documentacao.placa = novos_dados_carro["placa"]
            carro.quilometragem = novos_dados_carro["quilometragem"]
            carro.unidades_existentes = novos_dados_carro["unidades_existentes"]
            self.lista_carros()
        else:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Carro não encontrado.")

    # Realiza a substituição das peças de um carro após selecioná-lo.
    def troca_peca(self):
        self.lista_carros()
        vin_carro = self.__tela_carro_classico.seleciona_carro()
        carro = self.pega_carro_por_vin(vin_carro)

        # Valida a existência do carro antes de prosseguir com a troca das peças.
        if carro is None:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Carro não encontrado.")
            return

        # Obtém e verifica as novas peças a serem associadas ao carro.
        motor, roda, pintura = self.obtem_e_verifica_pecas(vin_carro)

        if not motor or not roda or not pintura:
            return

        # Realiza a troca das peças.
        carro.motor = motor
        carro.roda = roda
        carro.pintura = pintura

        self.__tela_carro_classico.mostra_mensagem("Peças trocadas com sucesso!")
        self.lista_carros()

    # Exibe todos os carros cadastrados, mostrando VIN, modelo, ano e unidades existentes.
    def lista_carros(self): 
        if not self.__carros:
            self.__tela_carro_classico.mostra_mensagem("A lista de carros está vazia.")
            return
        
        for carro in self.__carros:
            self.__tela_carro_classico.mostra_carro({
                "vin": carro.documentacao.vin,
                "modelo": carro.documentacao.modelo,
                "ano": carro.documentacao.ano,
                "unidades_existentes": carro.unidades_existentes
            })

    # Exclui um carro da lista e atualiza os dados de cadastro.
    def exclui_carro(self):
        self.lista_carros()
        vin_carro = self.__tela_carro_classico.seleciona_carro()
        carro = self.pega_carro_por_vin(vin_carro)

        # Remove o carro da lista, se encontrado.
        if carro is not None:
            self.__carros.remove(carro)
            self.__controlador_sistema.controlador_pessoas.remove_carro(vin_carro)
            self.__tela_carro_classico.mostra_mensagem("Carro removido com sucesso!")
            self.lista_carros()
        else:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Carro não encontrado.")

    # Adiciona um valor de venda ao carro, se ele ainda não foi vendido
    def vende_carro(self, vin, preco):
        carro = self.pega_carro_por_vin(vin)

        if carro is not None and len(carro.precos_venda) <= len(carro.precos_compra):
            carro.add_preco_venda(preco)
            return True

        return False

    # Adiciona um valor de compra ao carro, se ele ainda não foi comprado
    def compra_carro(self, vin, preco):
        carro = self.pega_carro_por_vin(vin)

        if carro is not None and len(carro.precos_venda) == len(carro.precos_compra):
            if self.__controlador_sistema.controlador_inspecao.inclui_inspecao(vin, carro):
                carro.add_preco_venda(preco)
                return True
        return False

    # Verifica se a peça já está sendo utilizada
    def verifica_disponibilidade_peca(self, tipo_peca, identificador, carro_atual=""):
        for carro in self.__carros:
            if carro_atual == "" or carro.documentacao.vin != carro_atual:
                if tipo_peca == "motor" and carro.motor.num_motor == identificador:
                    return True
                elif tipo_peca == "roda" and carro.roda.num_serie == identificador:
                    return True
                elif tipo_peca == "pintura" and carro.pintura.codigo_cor == identificador:
                    return True
        return False

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_carro,
            2: self.altera_carro,
            3: self.lista_carros,
            4: self.exclui_carro,
            5: self.troca_peca,
            0: self.__controlador_sistema.abre_tela
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_carro_classico.tela_opcoes()]()