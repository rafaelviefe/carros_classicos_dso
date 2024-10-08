class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Concessionária Clássica ---------")
        print("Escolha sua opcao")
        print("1 - Clientes")
        print("2 - Carros")
        print("3 - Inspeções")
        print("4 - Peças")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao