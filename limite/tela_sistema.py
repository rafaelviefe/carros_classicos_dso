class TelaSistema:
    def tela_opcoes(self):
        opcao = -1
        while opcao not in [0, 1, 2, 3, 4]:
            try:
                print()
                print("-------- Concessionária Clássica ---------")
                print("Escolha sua opcao")
                print("1 - Clientes")
                print("2 - Carros")
                print("3 - Inspeções")
                print("4 - Peças")
                print("0 - Finalizar sistema")
                print()
                
                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3, 4]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao
