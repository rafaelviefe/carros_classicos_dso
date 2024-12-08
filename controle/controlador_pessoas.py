from limite.tela_pessoa import TelaPessoa
from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante

from exception.inclusao_exception import InclusaoException
from exception.exclusao_exception import ExclusaoException
from exception.listagem_exception import ListagemException
from exception.alteracao_exception import AlteracaoException

from DAOs.pessoa_dao import PessoaDAO

class ControladorPessoas():

  def __init__(self, controlador_sistema):
    self.__pessoa_DAO = PessoaDAO()
    self.__tela_pessoa = TelaPessoa()
    self.__controlador_sistema = controlador_sistema

  # Busca uma pessoa na lista pelo documento fornecido
  def pega_pessoa_por_doc(self, documento: str):
    for pessoa in self.__pessoa_DAO.get_all():
      if pessoa.documento == documento:
        return pessoa
    return None

  # Inclui uma nova pessoa (Negociante ou Pessoa Jurídica) após validar a unicidade do documento
  def inclui_pessoa(self):
      try:
          dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()

          if any(pessoa.documento == dados_pessoa["documento"] for pessoa in self.__pessoa_DAO.get_all()):
              raise InclusaoException("Uma pessoa com este documento já foi registrada.")
          
          if len(dados_pessoa["documento"]) == 11:
              pessoa = Negociante(dados_pessoa["nome"], dados_pessoa["documento"])
          else:
              pessoa = PessoaJuridica(dados_pessoa["nome"], dados_pessoa["documento"])

          self.__pessoa_DAO.add(pessoa)
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

        self.__pessoa_DAO.update(pessoa)
        self.lista_pessoas()

    except AlteracaoException as e:
        self.__tela_pessoa.mostra_mensagem(f"ATENÇÃO: {str(e)}")

  # Exibe uma lista de todas as pessoas registradas
  def lista_pessoas(self):
      pessoas = self.__pessoa_DAO.get_all()

      try:
          if not pessoas:
              raise ListagemException("A lista de pessoas está vazia.")

          lista_pessoas_com_carros = []
          for pessoa in pessoas:
              carros = self.__controlador_sistema.controlador_transferencias.pega_carros_por_documento(pessoa.documento)
              lista_carros = [
                  {
                      "vin": carro.documentacao.vin,
                      "modelo": carro.documentacao.modelo,
                      "ano": carro.documentacao.ano,
                  }
                  for carro in carros
              ]
              lista_pessoas_com_carros.append({
                  "nome": pessoa.nome,
                  "documento": pessoa.documento,
                  "carros": lista_carros,
              })

          self.__tela_pessoa.mostra_pessoas(lista_pessoas_com_carros)

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

          self.__pessoa_DAO.remove(pessoa.documento)
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
