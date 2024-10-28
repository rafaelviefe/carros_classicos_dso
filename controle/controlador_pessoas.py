from limite.tela_pessoa import TelaPessoa
from entidade.pessoa_juridica import PessoaJuridica
from entidade.negociante import Negociante

class ControladorPessoas():

  def __init__(self, controlador_sistema):
    self.__pessoas = []
    self.__tela_pessoa = TelaPessoa()
    self.__controlador_sistema = controlador_sistema

  def pega_pessoa_por_doc(self, documento: str):
    for pessoa in self.__pessoas:
      if(pessoa.documento == documento):
        return pessoa
    return None

  def inclui_pessoa(self):
    dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        
    if any(pessoa.documento == dados_pessoa["documento"] for pessoa in self.__pessoas):
      self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Uma pessoa com este documento já foi registrada.")
      return
    
    if len(dados_pessoa["documento"]) == 11:
      pessoa = Negociante(dados_pessoa["nome"], dados_pessoa["documento"])

    else:
      pessoa = PessoaJuridica(dados_pessoa["nome"], dados_pessoa["documento"])

    self.__pessoas.append(pessoa)
    self.lista_pessoas()

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

  def lista_pessoas(self):
    if not self.__pessoas:
      self.__tela_pessoa.mostra_mensagem("A lista de pessoas está vazia.")
      return
    
    for pessoa in self.__pessoas:
      self.__tela_pessoa.mostra_pessoa({"nome": pessoa.nome, "documento": pessoa.documento, "carros": pessoa.carros})

  def exclui_pessoa(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      self.__pessoas.remove(pessoa)
      self.lista_pessoas()
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não existente")

  def registra_compra(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      dados_compra = self.__tela_pessoa.seleciona_carro()
      doc_carro, valor = dados_compra[0], dados_compra[1]

      if self.__controlador_sistema.controlador_carros_classicos.vende_carro(doc_carro, valor):
        carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(doc_carro)
        pessoa.add_carro(carro)
        self.lista_pessoas()

      else:
        self.__tela_pessoa.mostra_mensagem("ATENCAO: Carro não encontrado ou já vendido")
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  def registra_venda(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      dados_compra = self.__tela_pessoa.seleciona_carro()
      doc_carro, valor = dados_compra[0], dados_compra[1]

      if self.__controlador_sistema.controlador_carros_classicos.compra_carro(doc_carro, valor):
        carro = self.__controlador_sistema.controlador_carros_classicos.pega_carro_por_vin(doc_carro)
        pessoa.del_carro(carro)
        self.lista_pessoas()

      else:
        self.__tela_pessoa.mostra_mensagem("ATENCAO: Carro não encontrado ou já comprado")
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  def abre_tela(self):
    lista_opcoes = {1: self.inclui_pessoa, 2: self.altera_pessoa, 3: self.lista_pessoas, 4: self.exclui_pessoa, 5: self.registra_compra, 6: self.registra_venda, 0: self.__controlador_sistema.abre_tela}

    continua = True
    while continua:
      lista_opcoes[self.__tela_pessoa.tela_opcoes()]()

