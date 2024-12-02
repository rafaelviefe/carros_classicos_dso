from entidade.transferencia import Transferencia
from limite.tela_transferencia import TelaTransferencia

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException
from exception.alteracao_exception import AlteracaoException

class ControladorTransferencias:
    def __init__(self, controlador_sistema):
        self.__transferencias = []
        self.__tela_transferencia = TelaTransferencia()
        self.__controlador_sistema = controlador_sistema
        self.__id_transferencia = 0

    def gera_id(self):
        self.__id_transferencia += 1
        return self.__id_transferencia

    # Verifica a última transferência de um carro
    def ultima_transferencia(self, vin):
        transferencias_carro = [
            transf for transf in self.__transferencias if transf.carro_vin == vin
        ]
        return transferencias_carro[-1] if transferencias_carro else None

    # Inclui uma nova transferência
    def inclui_transferencia(self):
        try:
            dados_transferencia = self.__tela_transferencia.pega_dados_transferencia()
            vin = dados_transferencia["carro_vin"]
            tipo = dados_transferencia["tipo"]
            comprador_vendedor_doc = dados_transferencia["documento"]

            carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(vin)
            if not carro:
                raise InclusaoException("Carro não encontrado.")

            ultima_transf = self.ultima_transferencia(vin)

            if tipo == "compra":
                if ultima_transf and ultima_transf.tipo == "compra":
                    raise InclusaoException("Este carro já foi comprado e não pode ser comprado novamente.")
                
                aprovado = self.__controlador_sistema.controlador_assoc_carro_inspecao.inclui_inspecao(vin, carro)
                if not aprovado:
                    raise InclusaoException("O carro não passou na inspeção e não pode ser comprado.")
                
                if ultima_transf and ultima_transf.tipo == "venda":
                    vendedor_doc = ultima_transf.documento
                    if vendedor_doc != comprador_vendedor_doc:
                        raise InclusaoException("O vendedor informado não possui este carro.")

            elif tipo == "venda":
                if not ultima_transf or ultima_transf.tipo == "venda":
                    raise InclusaoException("Este carro não está disponível para venda.")
                
            id_transferencia = self.gera_id()
            transferencia = Transferencia(
                id=id_transferencia,
                documento_pessoa=comprador_vendedor_doc,
                carro_vin=vin,
                tipo=tipo,
                valor=dados_transferencia["valor"]
            )
            self.__transferencias.append(transferencia)
            self.__tela_transferencia.mostra_mensagem("Transferência registrada com sucesso!")
            self.lista_transferencias()

        except InclusaoException as e:
            self.__tela_transferencia.mostra_mensagem(f"ATENÇÃO: {str(e)}")

    def lista_transferencias(self):
        vin = self.__tela_transferencia.pega_vin()

        try:
            transferencias_filtradas = [trans for trans in self.__transferencias if trans.vin_carro == vin]

            if not transferencias_filtradas:
                raise ListagemException(f"Nenhuma transferência encontrada para o VIN {vin}.")

            for trans in transferencias_filtradas:
                atributos = {
                    "id": trans.id,
                    "documento_pessoa": trans.documento_pessoa,
                    "vin_carro": trans.documento_pessoa,
                    "tipo": trans.tipo,
                    "valor": trans.valor
                }
                self.__tela_transferencia.mostra_transferencia(atributos)

            return transferencias_filtradas

        except ListagemException as e:
            self.__tela_transferencia.mostra_mensagem(str(e))

    def altera_transferencia(self):
        try:
            transferencias = self.lista_transferencias()
            if not transferencias:
                return

            id_selecionado = self.__tela_transferencia.pega_id()
            transferencia = next((trans for trans in transferencias if trans.id == id_selecionado), None)

            if not transferencia:
                raise AlteracaoException("Transferência com o ID fornecido não encontrada.")

            novos_dados = self.__tela_transferencia.pega_alteracoes_transferencia()
            transferencia.documento_pessoa = novos_dados["documento_pessoa"]
            transferencia.vin_carro = novos_dados["vin_carro"]
            transferencia.valor = novos_dados["valor"]

            self.__tela_transferencia.mostra_mensagem("Transferência alterada com sucesso!")

        except (AlteracaoException, ListagemException) as e:
            self.__tela_transferencia.mostra_mensagem(str(e))

    def exclui_transferencia(self):
        try:
            transferencias = self.lista_transferencias()
            if not transferencias:
                return

            id_selecionado = self.__tela_transferencia.pega_id()
            transferencia = next((trans for trans in transferencias if trans.id == id_selecionado), None)

            if not transferencia:
                raise ExclusaoException("Transferência com o ID fornecido não encontrada.")

            self.__transferencias.remove(transferencia)
            self.__tela_transferencia.mostra_mensagem("Transferência excluída com sucesso!")

        except (ExclusaoException, ListagemException) as e:
            self.__tela_transferencia.mostra_mensagem(str(e))

    def pega_carros_por_documento(self, documento: str):
        carros = []
        verificados = []
        for transferencia in reversed(self.__transferencias):
            vin = transferencia.vin_carro
            if vin not in verificados:
                verificados.append(vin)
                if transferencia.tipo == "venda" and transferencia.documento_pessoa == documento:
                    carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(transferencia.vin_carro)
                    if carro and carro not in carros:
                        carros.append(carro)
        return carros
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_transferencia,
            2: self.altera_transferencia,
            3: self.lista_transferencias,
            4: self.exclui_transferencia,

            0: self.__controlador_sistema.abre_tela
        }
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_associacao.tela_opcoes()]()