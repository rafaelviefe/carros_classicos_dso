import re

class TelaPessoa:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3, 4, 5, 6]:
            try:
                print()
                print("-------- PESSOAS ----------")
                print("Escolha a opcao")
                print("1 - Incluir Pessoa")
                print("2 - Alterar Pessoa")
                print("3 - Listar Pessoas")
                print("4 - Excluir Pessoa")
                print("0 - Retornar")
                print()

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3, 4]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao

    def pega_dados_pessoa(self):
        nome = input("Nome: ").strip()
        while not nome:
            print("Nome inválido! O nome não pode ser vazio.")
            nome = input("Nome: ").strip()

        documento = input("Documento (CPF ou CNPJ): ").strip()
        while not self.validar_documento(documento):
            print("Documento inválido! Por favor, insira um CPF ou CNPJ válido.")
            documento = input("Documento (CPF ou CNPJ): ").strip()

        return {"nome": nome, "documento": documento}

    # Remove todos os não digitos do documento e decide entre cpf e cnpj
    def validar_documento(self, documento: str) -> bool:
        documento = re.sub(r'\D', '', documento)
        if len(documento) == 11:
            return self.validar_cpf(documento)
        elif len(documento) == 14:
            return self.validar_cnpj(documento)
        else:
            return False

    # Algorítimo padrão para validar cpf
    def validar_cpf(self, cpf: str) -> bool:
        if cpf == cpf[0] * len(cpf):
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return cpf[-2:] == f"{digito1}{digito2}"

    # Algorítimo padrão para validar cnpj
    def validar_cnpj(self, cnpj: str) -> bool:
        if cnpj == cnpj[0] * len(cnpj):
            return False

        def calcula_digito(cnpj, peso):
            soma = sum(int(cnpj[i]) * peso[i] for i in range(len(peso)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        digito1 = calcula_digito(cnpj[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

        digito2 = calcula_digito(cnpj[:13], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

        return cnpj[-2:] == f"{digito1}{digito2}"
    
    def pega_novo_nome(self):
        novo_nome = input("Novo nome: ").strip()
        while not novo_nome:
            print("Nome inválido! O nome não pode ser vazio.")
            novo_nome = input("Novo nome: ").strip()
        return novo_nome

    def mostra_pessoa(self, dados_pessoa):
        print()
        print("Nome do cliente:", dados_pessoa["nome"])
        print("Documento do cliente:", dados_pessoa["documento"])
        print()

    def mostra_carro(self, dados_carro):
        print("  Vin:", dados_carro["vin"])
        print("  Modelo:", dados_carro["modelo"])
        print("  Ano:", dados_carro["ano"])
        print()

    def seleciona_pessoa(self):
        documento = input("Documento do cliente que deseja selecionar: ").strip()
        while not documento:
            print("Documento inválido! O documento não pode ser vazio.")
            documento = input("Documento do cliente que deseja selecionar: ").strip()

        return documento
    
    def mostra_mensagem(self, msg):
        print(msg)