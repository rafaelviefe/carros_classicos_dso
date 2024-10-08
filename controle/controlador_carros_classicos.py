from limite.tela_carro_classico import TelaCarroClassico
from entidade.carro_classico import CarroClassico

class ControladorCarrosClassicos():

  def __init__(self, controlador_sistema):
    self.__carros = []
    self.__tela_carro_classico = TelaCarroClassico()
    self.__controlador_sistema = controlador_sistema

  def pega_carro_por_vin(self, vin: str):
    for carro in self.__carros:
      if(carro.vin == vin):
        return carro
    return None
  
  def vender_carro(self, vin, preco):
    carro = self.pega_carro_por_vin(vin)

    if (not carro == None) and (len(carro.preco_venda) <= len(carro.preco_compra)):
      carro.add_preco_venda(preco)
      return True
    
    return False

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_pessoa, 2: self.alterar_pessoa, 3: self.lista_pessoas, 4: self.excluir_pessoa, 5: self.registrar_compra, 6: self.registrar_venda, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_pessoa.tela_opcoes()]()

