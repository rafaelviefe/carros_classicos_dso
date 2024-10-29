from controle.controlador_assoc_carro_inspecao import ControladorAssocCarroInspecao

class TelaAssocCarroInspecao:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3]:
            try:
                print("-------- ASSOCIAÇÃO CARROS E INSPEÇÃO ----------")
                print("Escolha a opcao")
                print("1 - Incluir associação")
                print("2 - Listar associação")
                print("3 - Excluir associação")
                print("0 - Retornar")

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao
        
    def pegar_vin(self):
        # tratar exceçao
        vin = input("Vin do carro: ").strip()
        while not self.validar_vin(vin):
            print("Documento inválido! Por favor, insira uma vin válida.")
            vin = input("Vin do carro: ").strip()
        return vin  
    
    def validar_vin(self, vin):
        for carro in ControladorAssocCarroInspecao.lista_carros:
            if(carro.vin == vin):
                return True
            return False

    def pegar_id(self, inspecoes):
       id = input("ID da inspeção: ").strip()
       return id

    def pegar_dados_carro_classico(self):
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
        
        return{
            "num_motor": num_motor,
            "num_serie": num_serie,
            "codigo_cor": codigo_cor
        }


    def mostra_inspecao(self, inspecao):
        print("\n")
        print("Número de ID: ", inspecao.id)
        print("Vin do carro: ", inspecao.carro.documento.vin)
        print("Apto: ", inspecao.apto)
        print("Resultado: ", inspecao.resultado)
        print("\n")

      
            


