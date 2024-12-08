from limite.tela_carro_classico import TelaCarroClassico
from entidade.carro_classico import CarroClassico

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException
from exception.alteracao_exception import AlteracaoException

from DAOs.carro_classico_dao import CarroClassicoDAO

class ControladorCarrosClassicos:

    def __init__(self, controlador_sistema):
        self.__carro_classico_DAO = CarroClassicoDAO()
        self.__tela_carro_classico = TelaCarroClassico()
        self.__controlador_sistema = controlador_sistema

    # Busca um carro na lista de carros pelo número VIN e o retorna.
    def pega_carro_por_vin(self, vin: str):
        for carro in self.__carro_classico_DAO.get_all():
            if carro.documentacao.vin == vin:
                return carro
        return None

    # Obtém e valida as peças do carro; lança exceção em caso de erro
    def obtem_e_verifica_pecas(self, carro_atual=""):
        pecas_carro = self.__tela_carro_classico.pega_pecas_carro()

        motor = self.__controlador_sistema.controlador_pecas.pega_motor_por_num(pecas_carro["num_motor"])
        roda = self.__controlador_sistema.controlador_pecas.pega_roda_por_num(pecas_carro["num_serie"])
        pintura = self.__controlador_sistema.controlador_pecas.pega_pintura_por_cod(pecas_carro["codigo_cor"])

        # Lança exceção se uma peça não for encontrada
        if not motor:
            raise InclusaoException("Motor não encontrado. Verifique o número informado.")
        if not roda:
            raise InclusaoException("Roda não encontrada. Verifique o número de série informado.")
        if not pintura:
            raise InclusaoException("Pintura não encontrada. Verifique o código de cor informado.")

        # Verifica se as peças estão disponíveis (não associadas a outros carros)
        if self.verifica_disponibilidade_peca("motor", motor.num_motor, carro_atual):
            raise InclusaoException("Este motor já está associado a outro carro.")
        if self.verifica_disponibilidade_peca("roda", roda.num_serie, carro_atual):
            raise InclusaoException("Esta roda já está associada a outro carro.")
        if self.verifica_disponibilidade_peca("pintura", pintura.codigo_cor, carro_atual):
            raise InclusaoException("Esta pintura já está associada a outro carro.")

        return motor, roda, pintura

    # Inclui um novo carro na lista após verificar as peças e obter os dados do carro.
    def inclui_carro(self):
        try:
            motor, roda, pintura = self.obtem_e_verifica_pecas()
            dados_carro = self.__tela_carro_classico.pega_dados_carro()
            
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
            
            self.__carro_classico_DAO.add(carro)
            self.lista_carros()
        
        except InclusaoException as e:
            self.__tela_carro_classico.mostra_mensagem(f"ATENÇÃO: {e}")
        
        except TypeError as e:
            raise InclusaoException(f"Erro ao criar o carro: {e}")

    # Modifica os dados de um carro existente na lista.
    def altera_carro(self):
        try:
            self.lista_carros()
            vin_carro = self.__tela_carro_classico.seleciona_carro()
            carro = self.pega_carro_por_vin(vin_carro)

            if carro is None:
                raise AlteracaoException("Carro não encontrado para alteração.")

            # Atualiza os atributos do carro se ele for encontrado.
            novos_dados_carro = self.__tela_carro_classico.pega_alteracoes_carro()
            carro.documentacao.placa = novos_dados_carro["placa"]
            carro.quilometragem = novos_dados_carro["quilometragem"]
            carro.unidades_existentes = novos_dados_carro["unidades_existentes"]

            self.__carro_classico_DAO.update(carro)
            self.lista_carros()

        except AlteracaoException as e:
            self.__tela_carro_classico.mostra_mensagem(f"ATENÇÃO: {e}")

    # Realiza a substituição das peças de um carro após selecioná-lo.
    def troca_peca(self):
        try:
            self.lista_carros()
            vin_carro = self.__tela_carro_classico.seleciona_carro()
            carro = self.pega_carro_por_vin(vin_carro)

            # Valida a existência do carro antes de prosseguir com a troca das peças.
            if carro is None:
                raise AlteracaoException("Carro não encontrado para troca de peças.")

            motor, roda, pintura = self.obtem_e_verifica_pecas(vin_carro)

            if not motor or not roda or not pintura:
                raise AlteracaoException("Erro na verificação das novas peças para troca.")

            # Realiza a troca das peças.
            carro.motor = motor
            carro.roda = roda
            carro.pintura = pintura

            self.__carro_classico_DAO.update(carro)
            self.__tela_carro_classico.mostra_mensagem("Peças trocadas com sucesso!")
            self.lista_carros()

        except InclusaoException as e:
            self.__tela_carro_classico.mostra_mensagem(f"ATENÇÃO: {e}")
            
        except AlteracaoException as e:
            self.__tela_carro_classico.mostra_mensagem(f"ATENÇÃO: {e}")

    # Exibe todos os carros cadastrados, mostrando VIN, modelo, ano e unidades existentes.
    def lista_carros(self): 
        try:
            carros = self.__carro_classico_DAO.get_all()

            if not carros:
                raise ListagemException("A lista de carros está vazia.")
            
            for carro in carros:
                self.__tela_carro_classico.mostra_carro({
                    "vin": carro.documentacao.vin,
                    "modelo": carro.documentacao.modelo,
                    "ano": carro.documentacao.ano,
                    "unidades_existentes": carro.unidades_existentes
                })
        
        except ListagemException as e:
            self.__tela_carro_classico.mostra_mensagem(str(e))

    # Exclui um carro da lista e atualiza os dados de cadastro.
    def exclui_carro(self):
        try:
            self.lista_carros()
            vin_carro = self.__tela_carro_classico.seleciona_carro()
            carro = self.pega_carro_por_vin(vin_carro)

            if not carro:
                raise ExclusaoException("ATENÇÃO: Carro não encontrado.")
            
            self.__carro_classico_DAO.remove(carro.documentacao.vin)
            self.__tela_carro_classico.mostra_mensagem("Carro removido com sucesso!")
            self.lista_carros()
            
        except ExclusaoException as e:
            self.__tela_carro_classico.mostra_mensagem(str(e))

    # Verifica se a peça já está sendo utilizada
    def verifica_disponibilidade_peca(self, tipo_peca, identificador, carro_atual=""):
        for carro in self.__carro_classico_DAO.get_all():
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