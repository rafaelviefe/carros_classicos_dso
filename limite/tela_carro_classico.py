class TelaCarroClassico:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3, 4, 5]:
            try:
                print("\n")
                print("-------- CARROS CLÁSSICOS ----------")
                print("Escolha a opcao")
                print("1 - Incluir Carro")
                print("2 - Alterar Carro")
                print("3 - Listar Carros")
                print("4 - Excluir Carro")
                print("5 - Trocar Peças")
                print("0 - Retornar")
                print("\n")

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao

    def pega_dados_carro(self):
        vin = input("VIN: ").strip()
        while not vin:
            print("VIN inválido! O VIN não pode ser vazio.")
            vin = input("VIN: ").strip()

        placa = input("Placa: ").strip()
        while not placa:
            print("Placa inválida! A placa não pode ser vazia.")
            placa = input("Placa: ").strip()

        modelo = input("Modelo: ").strip()
        while not modelo:
            print("Modelo inválido! O modelo não pode ser vazio.")
            modelo = input("Modelo: ").strip()

        input_valido = False
        while not input_valido:
            try:
                ano = int(input("Ano: ").strip())
                input_valido = True
            except ValueError:
                print("Ano inválido! Por favor, insira um número inteiro.")

        input_valido = False
        while not input_valido:
            try:
                quilometragem = float(input("Quilometragem: ").strip())
                input_valido = True
            except ValueError:
                print("Quilometragem inválida! Por favor, insira um número decimal.")

        cambio = input("Tipo de câmbio: ").strip()
        while not cambio:
            print("Tipo de câmbio inválido! O tipo de câmbio não pode ser vazio.")
            cambio = input("Tipo de câmbio: ").strip()

        input_valido = False
        while not input_valido:
            try:
                unidades_existentes = int(input("Unidades existentes: ").strip())
                input_valido = True
            except ValueError:
                print("Unidades existentes inválidas! Por favor, insira um número inteiro.")

        return {
            "vin": vin,
            "placa": placa,
            "modelo": modelo,
            "ano": ano,
            "quilometragem": quilometragem,
            "cambio": cambio,
            "unidades_existentes": unidades_existentes,
        }

    def pega_alteracoes_carro(self):
        placa = input("Nova Placa: ").strip()
        while not placa:
            print("Placa inválida! A placa não pode ser vazia.")
            placa = input("Nova Placa: ").strip()

        input_valido = False
        while not input_valido:
            try:
                quilometragem = float(input("Nova Quilometragem: ").strip())
                input_valido = True
            except ValueError:
                print("Quilometragem inválida! Por favor, insira um número decimal.")

        input_valido = False
        while not input_valido:
            try:
                unidades_existentes = int(input("Unidades existentes: ").strip())
                input_valido = True
            except ValueError:
                print("Unidades existentes inválidas! Por favor, insira um número inteiro.")

        return {
            "placa": placa,
            "quilometragem": quilometragem,
            "unidades_existentes": unidades_existentes,
        }

    def pega_pecas_carro(self):
        num_motor = input("Número do Motor: ").strip()
        num_serie = input("Número de Série da Roda: ").strip()
        codigo_cor = input("Código da Pintura: ").strip()

        return {
            "num_motor": num_motor,
            "num_serie": num_serie,
            "codigo_cor": codigo_cor
        }

    def seleciona_carro(self):
        vin = input("VIN do carro que deseja selecionar: ").strip()
        while not vin:
            print("VIN inválido! O VIN não pode ser vazio.")
            vin = input("VIN do carro que deseja selecionar: ").strip()
        return vin

    def mostra_carro(self, dados_carro):
        print("\n")
        print("VIN: ", dados_carro["vin"])
        print("Modelo: ", dados_carro["modelo"])
        print("Ano: ", dados_carro["ano"])
        print("Unidades Existentes: ", dados_carro["unidades_existentes"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)
