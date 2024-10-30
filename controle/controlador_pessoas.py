from limite.tela_pessoa import TelaPessoa
from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException

class ControladorPessoas():

  def __init__(self, controlador_sistema):
    self.__pessoas = []
    self.__tela_pessoa = TelaPessoa()
    self.__controlador_sistema = controlador_sistema

  # Busca uma pessoa na lista pelo documento fornecido
  def pega_pessoa_por_doc(self, documento: str):
    for pessoa in self.__pessoas:
      if pessoa.documento == documento:
        return pessoa
    return None

  # Inclui uma nova pessoa (Negociante ou Pessoa Jurídica) após validar a unicidade do documento
  def inclui_pessoa(self):
      try:
          dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()

          if any(pessoa.documento == dados_pessoa["documento"] for pessoa in self.__pessoas):
              raise InclusaoException("Uma pessoa com este documento já foi registrada.")
          
          if len(dados_pessoa["documento"]) == 11:
              pessoa = Negociante(dados_pessoa["nome"], dados_pessoa["documento"])
          else:
              pessoa = PessoaJuridica(dados_pessoa["nome"], dados_pessoa["documento"])

          self.__pessoas.append(pessoa)
          self.lista_pessoas()

      except InclusaoException as e:
          self.__tela_pessoa.mostra_mensagem(f"ATENÇÃO: {str(e)}")

  # Permite alterar o nome de uma pessoa após selecioná-la pelo documento
  def altera_pessoa(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if pessoa is not None:
      novo_nome = self.__tela_pessoa.pega_novo_nome()
      pessoa.nome = novo_nome
      self.lista_pessoas()
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  # Exibe uma lista de todas as pessoas registradas
  def lista_pessoas(self):
      try:
          if not self.__pessoas:
              raise ListagemException("A lista de pessoas está vazia.")

          # Exibe os detalhes das pessoas
          for pessoa in self.__pessoas:
              self.__tela_pessoa.mostra_pessoa({"nome": pessoa.nome, "documento": pessoa.documento, "carros": pessoa.carros})

      except ListagemException as e:
          self.__tela_pessoa.mostra_mensagem(f"ATENÇÃO: {str(e)}")

  # Remove uma pessoa da lista após selecioná-la pelo documento
  def exclui_pessoa(self):
      try:
          self.lista_pessoas()
          doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
          pessoa = self.pega_pessoa_por_doc(doc_pessoa)

          if pessoa is None:
              raise ExclusaoException("Pessoa não existente.")

          self.__pessoas.remove(pessoa)
          self.lista_pessoas()

      except ExclusaoException as e:
          self.__tela_pessoa.mostra_mensagem(f"ATENÇÃO: {str(e)}")

  # Registra uma compra de carro para uma pessoa, associando o carro à pessoa selecionada
  def registra_compra(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if pessoa is not None:
      dados_compra = self.__tela_pessoa.seleciona_carro()
      doc_carro, valor = dados_compra[0], dados_compra[1]

      # Verifica disponibilidade do carro e registra a compra
      if self.__controlador_sistema.controlador_carros_classicos.vende_carro(doc_carro, valor):
        carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(doc_carro)
        pessoa.add_carro(carro)
        self.__tela_pessoa.mostra_mensagem("Venda realizada com sucesso!")
        self.lista_pessoas()
      else:
        self.__tela_pessoa.mostra_mensagem("ATENCAO: Carro não encontrado ou já vendido")
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  # Registra uma venda de carro para uma pessoa, removendo o carro da lista de carros da pessoa
  def registra_venda(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if pessoa is not None:
        dados_compra = self.__tela_pessoa.seleciona_carro()
        doc_carro, valor = dados_compra[0], dados_compra[1]

        # Verifica se o carro realmente pertence à pessoa antes de registrar a venda
        carro = next((c for c in pessoa.carros if c.documentacao.vin == doc_carro), None)
        
        if carro is None:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Este carro não pertence à pessoa selecionada.")
            return

        # Verifica disponibilidade para compra e realiza a transação
        if self.__controlador_sistema.controlador_carros_classicos.compra_carro(doc_carro, valor):
            pessoa.del_carro(carro)
            self.__tela_pessoa.mostra_mensagem("Compra realizada com sucesso!")
            self.lista_pessoas()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Carro não encontrado ou já comprado")
    else:
        self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não encontrada")

  # Remove um carro específico de uma pessoa pelo VIN
  def remove_carro(self, vin: str) -> bool:
      for pessoa in self.__pessoas:
          for carro in pessoa.carros:
              if carro.documentacao.vin == vin:
                  pessoa.carros.remove(carro)
                  return True
      return False

  # Exibe a tela de opções do sistema e chama o método correspondente à seleção
  def abre_tela(self):
    lista_opcoes = {
      1: self.inclui_pessoa, 
      2: self.altera_pessoa, 
      3: self.lista_pessoas, 
      4: self.exclui_pessoa, 
      5: self.registra_compra, 
      6: self.registra_venda, 
      0: self.__controlador_sistema.abre_tela
    }

    continua = True
    while continua:
      lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
