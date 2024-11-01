class TelaAssocCarroInspecao:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            try:
                print()
                print("-------- INSPEÇÕES ----------")
                print("Escolha a opcao")
                print("1 - Incluir inspeção")
                print("2 - Listar inspeções")
                print("3 - Excluir inspeção")
                print()
                print("-------- REGISTROS ----------")
                print("4 - Incluir registro")
                print("5 - Excluir registro")
                print("6 - Alterar registro")
                print("7 - Listar registros")
                print("8 - Obter relatório")
                print()
                print("0 - Retornar")
                print()

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao
        
    def pega_vin(self):
        vin = input("Vin do carro: ").strip()
        while not vin:
            print("Documento inválido! Por favor, insira uma vin válida.")
            vin = input("Vin do carro: ").strip()
        return vin  
    
    def pega_id(self):
        id_valido = False
        while not id_valido:
            try:
                id_inspecao = int(input("Digite o ID da inspeção que deseja selecionar: ").strip())
                id_valido = True
            except ValueError:
                print("ID inválida! Por favor, insira um número inteiro.")
        return id_inspecao


    def pega_pecas_esperadas(self):
        num_motor = input("Número do Motor: ").strip()
        while not num_motor:
            print("Número do Motor inválido! O campo não pode ser vazio.")
            num_motor = input("Número do Motor: ").strip()
        
        num_serie = input("Número de Série: ").strip()
        while not num_serie:
            print("Número de Série inválido! O campo não pode ser vazio.")
            num_serie = input("Número de Série: ").strip()

        codigo_cor = input("Código da Cor: ").strip()
        while not codigo_cor:
            print("Código da cor inválido! O campo não pode ser vazio.")
            codigo_cor = input("Código da Cor: ").strip()
        
        return {
            "motor": num_motor,
            "roda": num_serie,
            "pintura": codigo_cor
        }

    def mostra_inspecao(self, assoc):
        print()
        print("Número de ID:", assoc.id)
        print("Apto:", "Sim" if assoc.inspecao.apto else "Não")
        print("Resultado:", assoc.inspecao.resultado.capitalize())
        print()

    def mostra_inconstancias(self, pecas_diferentes):
        print()
        if pecas_diferentes:
            print("Peças diferentes encontradas:")
            for peca, valores in pecas_diferentes.items():
                atual, esperado = valores
                print(f"- {peca.capitalize()}: Atual -> {atual}, Esperado -> {esperado}")
        else:
            print("Nenhuma diferença encontrada nas peças.")

    def obtem_data(self):
        mes = -1
        ano = -1
        
        while mes < 1 or mes > 12:
            try:
                mes = int(input("Digite o mês (1-12): ").strip())
                if mes < 1 or mes > 12:
                    print("Mês inválido! Por favor, insira um valor entre 1 e 12.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro para o mês.")
        
        while ano < 0:
            try:
                ano = int(input("Digite o ano: ").strip())
                if ano < 0:
                    print("Ano inválido! Por favor, insira um valor inteiro positivo.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro para o ano.")
        
        data_formatada = f"{mes:02d}-{ano}"
        return data_formatada
    def mostra_mensagem(self, msg):
        print(msg)
