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

  def incluir_pessoa(self):
    dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        
    if any(pessoa.documento == dados_pessoa["documento"] for pessoa in self.__pessoas):
      self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Uma pessoa com este documento já foi registrada.")
      return
    
    if len(dados_pessoa["documento"]) == 11:
      pessoa = Negociante(dados_pessoa["nome"], dados_pessoa["documento"])

    else:
      pessoa = PessoaJuridica(dados_pessoa["nome"], dados_pessoa["documento"])

    self.__pessoas.append(pessoa)

  def alterar_pessoa(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
      pessoa.nome = novos_dados_pessoa["nome"]
      pessoa.cpf = novos_dados_pessoa["documento"]
      self.lista_amigos()
    else:
      self.__tela_amigo.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  def lista_pessoas(self):
    if not self.__pessoas:
      self.__tela_pessoa.mostra_mensagem("A lista de pessoas está vazia.")
      return
    
    for pessoa in self.__pessoas:
      self.__tela_pessoa.mostra_pessoa({"nome": pessoa.nome, "cpf": pessoa.cpf, "carros": pessoa.carros})

  def excluir_pessoa(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      self.__pessoas.remove(pessoa)
      self.lista_pessoas()
    else:
      self.__tela_pessoa.mostra_mensagem("ATENCAO: Pessoa não existente")

  def registrar_compra(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      doc_carro = self.__tela_pessoa.seleciona_carro()[0]
      valor = self.__tela_pessoa.seleciona_carro()[1]
      controle_carros.vender_carro(doc_carro, valor)
      carro = controle_carros.pega_carro_por_vin(doc_carro)
      pessoa.add_carro(carro)

    else:
      self.__tela_amigo.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  def registrar_venda(self):
    self.lista_pessoas()
    doc_pessoa = self.__tela_pessoa.seleciona_pessoa()
    pessoa = self.pega_pessoa_por_doc(doc_pessoa)

    if(pessoa is not None):
      doc_carro = self.__tela_pessoa.seleciona_carro()[0]
      valor = self.__tela_pessoa.seleciona_carro()[1]
      controle_carros.comprar_carro(doc_carro, valor)
      carro = controle_carros.pega_carro_por_vin(doc_carro)
      pessoa.carros.del_carro(carro)

    else:
      self.__tela_amigo.mostra_mensagem("ATENCAO: Pessoa não encontrada")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_pessoa, 2: self.alterar_pessoa, 3: self.lista_pessoas, 4: self.excluir_pessoa, 5: self.registrar_compra, 6: self.registrar_venda, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_pessoa.tela_opcoes()]()

