from limite.tela_pessoa import TelaPessoa
from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException
from exception.alteracao_exception import AlteracaoException

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
    try:
        self.lista_pessoas()
        doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_doc(doc_pessoa)

        if pessoa is None:
            raise AlteracaoException("Pessoa não encontrada. Verifique o documento informado.")
        
        novo_nome = self.__tela_pessoa.pega_novo_nome()
        pessoa.nome = novo_nome
        self.lista_pessoas()

    except AlteracaoException as e:
        self.__tela_pessoa.mostra_mensagem(f"ATENÇÃO: {str(e)}")

  # Exibe uma lista de todas as pessoas registradas
  def lista_pessoas(self):
    try:
      if not self.__pessoas:
            raise ListagemException("A lista de pessoas está vazia.")

      for pessoa in self.__pessoas:
        dados_pessoa = {
          "nome": pessoa.nome,
          "documento": pessoa.documento,
        }
        self.__tela_pessoa.mostra_pessoa(dados_pessoa)

        carros = self.__controlador_sistema.controlador_transferencias.pega_carros_por_documento(pessoa.documento)
        for carro in carros:
          dados_carro = {
            "vin": carro.documentacao.vin,
            "modelo": carro.documentacao.modelo,
            "ano": carro.documentacao.ano,
          }
          self.__tela_pessoa.mostra_carro(dados_carro)

    except ListagemException as e:
        self.__tela_pessoa.mostra_erro(str(e))

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

  # Exibe a tela de opções do sistema e chama o método correspondente à seleção
  def abre_tela(self):
    lista_opcoes = {
      1: self.inclui_pessoa, 
      2: self.altera_pessoa, 
      3: self.lista_pessoas, 
      4: self.exclui_pessoa, 

      0: self.__controlador_sistema.abre_tela
    }

    continua = True
    while continua:
      lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
