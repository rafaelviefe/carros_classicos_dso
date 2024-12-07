class TelaTransferencia:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3, 4]:
            try:
                print()
                print("-------- TRANSFERÊNCIAS ----------")
                print("Escolha a opção")
                print("1 - Incluir Transferência")
                print("2 - Alterar Transferência")
                print("3 - Listar Transferências")
                print("4 - Excluir Transferência")
                print()
                print("0 - Retornar")
                print()

                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3, 4]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao

    def pega_dados_transferencia(self):
        print("\nInforme os dados da transferência:")
        
        vin_carro = input("VIN do carro: ").strip()
        while not vin_carro:
            print("VIN inválido! Por favor, insira um VIN válido.")
            vin_carro = input("VIN do carro: ").strip()

        tipo = ""
        while tipo not in ["compra", "venda"]:
            tipo = input("Tipo de transferência (compra/venda): ").strip().lower()
            if tipo not in ["compra", "venda"]:
                print("Tipo inválido! Digite 'compra' ou 'venda'.")
        
        documento = input("Documento da pessoa (CPF/CNPJ): ").strip()
        while not documento:
            print("Documento inválido! O campo não pode ser vazio.")
            documento = input("Documento da pessoa (CPF/CNPJ): ").strip()

        valor = -1
        while valor <= 0:
            try:
                valor = float(input("Valor da transferência (R$): ").strip())
                if valor <= 0:
                    print("Valor inválido! Insira um valor maior que zero.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número para o valor.")

        return {
            "vin_carro": vin_carro,
            "tipo": tipo,
            "documento_pessoa": documento,
            "valor": valor,
        }

    def pega_alteracoes_transferencia(self):
        print("\nInforme os dados da transferência:")
        
        valor = -1
        while valor <= 0:
            try:
                valor = float(input("Valor da transferência (R$): ").strip())
                if valor <= 0:
                    print("Valor inválido! Insira um valor maior que zero.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número para o valor.")

        return {
            "valor": valor,
        }

    def pega_vin(self):
        vin = input("Digite o VIN do carro em questão: ").strip()
        while not vin:
            print("VIN inválido! Por favor, insira um VIN válido.")
            vin = input("Digite o VIN do carro em questão: ").strip()
        return vin

    def pega_id(self):
        id_transferencia = -1
        while id_transferencia < 0:
            try:
                id_transferencia = int(input("Digite o ID da transferência que deseja selecionar: ").strip())
                if id_transferencia < 0:
                    print("ID inválido! Insira um número positivo.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")
        return id_transferencia

    def mostra_transferencia(self, transferencia):
        print("\nDados da Transferência:")
        print(f"ID: {transferencia['id']}")
        print(f"VIN do carro: {transferencia['vin_carro']}")
        print(f"Tipo: {transferencia['tipo'].capitalize()}")
        print(f"Documento: {transferencia['documento_pessoa']}")
        print(f"Valor: R$ {transferencia['valor']:.2f}")
        print()

    def mostra_mensagem(self, msg):
        print(msg)
