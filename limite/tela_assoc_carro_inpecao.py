class TelaAssocCarroInspecao:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3]:
            try:
                print("-------- INSPEÇÕES ----------")
                print("Escolha a opcao")
                print("1 - Incluir inspeção")
                print("2 - Listar inspeções")
                print("3 - Excluir inspeção")
                print("0 - Retornar")

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3]:
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
        id_inspecao = input("Digite o ID da inspeção que deseja selecionar: ").strip()
        while not id_inspecao:
            print("ID inválida! O campo não pode ser vazio.")
            id_inspecao = input("Digite o ID da inspeção que deseja selecionar: ").strip()
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
            "num_motor": num_motor,
            "num_serie": num_serie,
            "codigo_cor": codigo_cor
        }

    def mostra_inspecao(self, assoc):
        print("\n")
        print("Número de ID: ", assoc.id)
        print("Vin do carro: ", assoc.carro.documento.vin)
        print("Apto: ", assoc.inspecao.apto)
        print("Resultado: ", assoc.inspecao.resultado)
        print("\n")

    def mostra_inconstancias(self, pecas_diferentes):
        if pecas_diferentes:
            print("Peças diferentes encontradas:")
            for peca, valores in pecas_diferentes.items():
                atual, esperado = valores
                print(f"- {peca.capitalize()}: Atual -> {atual}, Esperado -> {esperado}")
        else:
            print("Nenhuma diferença encontrada nas peças.")

    def mostra_mensagem(self, msg):
        print(msg)
