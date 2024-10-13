from limite.tela_carro_classico import TelaCarroClassico
from entidade.carro_classico import CarroClassico

class ControladorCarrosClassicos:

    def __init__(self, controlador_sistema):
        self.__carros = []
        self.__tela_carro_classico = TelaCarroClassico()
        self.__controlador_sistema = controlador_sistema

    def pega_carro_por_vin(self, vin: str):
        for carro in self.__carros:
            if carro.vin == vin:
                return carro
        return None

    def inclui_carro(self):
        pecas_carro = self.__tela_carro_classico.pega_pecas_carro()

        motor = self.__controlador_sistema.controle_pecas.pega_motor_por_num(pecas_carro["num_motor"])
        roda = self.__controlador_sistema.controle_pecas.pega_roda_por_num(pecas_carro["num_serie"])
        pintura = self.__controlador_sistema.controle_pecas.pega_pintura_por_cod(pecas_carro["codigo_cor"])

        if not motor or not roda or not pintura:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Uma ou mais peças não foram encontradas. Verifique os códigos e tente novamente.")
            return
        
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

        self.__carros.append(carro)
        self.lista_carros()

    def altera_carro(self):
      self.lista_carros()
      vin_carro = self.__tela_carro_classico.seleciona_carro()
      carro = self.pega_carro_por_vin(vin_carro)

      if carro is not None:
          novos_dados_carro = self.__tela_carro_classico.pega_alteracoes_carro()
          carro.placa = novos_dados_carro["placa"]
          carro.quilometragem = novos_dados_carro["quilometragem"]
          carro.unidades_existentes = novos_dados_carro["unidades_existentes"]
          self.lista_carros()
      else:
          self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Carro não encontrado.")

    def lista_carros(self):
        if not self.__carros:
            self.__tela_carro_classico.mostra_mensagem("A lista de carros está vazia.")
            return
        
        for carro in self.__carros:
            self.__tela_carro_classico.mostra_carro({
                "vin": carro.vin,
                "modelo": carro.modelo,
                "ano": carro.ano,
                "unidades_existentes": carro.unidades_existentes
            })

    def exclui_carro(self):
        self.lista_carros()
        vin_carro = self.__tela_carro_classico.seleciona_carro()
        carro = self.pega_carro_por_vin(vin_carro)

        if carro is not None:
            self.__carros.remove(carro)
            self.lista_carros()
        else:
            self.__tela_carro_classico.mostra_mensagem("ATENÇÃO: Carro não encontrado.")
  
    def vende_carro(self, vin, preco):
      carro = self.pega_carro_por_vin(vin)

      if (not carro == None) and (len(carro.preco_venda) <= len(carro.preco_compra)):
        carro.add_preco_venda(preco)
        return True
      
      return False
    
    def compra_carro(self, vin, preco):
      carro = self.pega_carro_por_vin(vin)

      if (not carro == None) and (len(carro.preco_venda) == len(carro.preco_compra)):
        if self.__controlador_sistema.controle_inspecao.fazer_inspecao(carro):
          carro.add_preco_venda(preco)
          return True
      
      return False

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_carro, 2: self.altera_carro, 3: self.lista_carros, 4: self.exclui_carro, 0: self.__controlador_sistema.abre_tela()}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_carro_classico.tela_opcoes()]()
