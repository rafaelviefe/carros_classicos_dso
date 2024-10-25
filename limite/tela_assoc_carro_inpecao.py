from controle.controlador_assoc_carro_inspecao import ControladorAssocCarroInspecao

class TelaAssocCarroInspecao:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3]:
            try:
                print("-------- ASSOCIAÇÃO CARROS E INSPEÇÃO ----------")
                print("Escolha a opcao")
                print("1 - Criar associação")
                print("2 - Listar associação")
                print("3 - Excluir associação")
                print("0 - Retornar")

                opcao = int(input("Escolha a opcao: "))
                if opcao not in [0, 1, 2, 3]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao
        
    def pegar_dados(self):
        # tratar exceçao
        placa = input("Placa do carro: ").strip()
        while not self.validar_placa(placa):
            print("Documento inválido! Por favor, insira uma placa válida.")
            placa = input("Placa do carro: ").strip()
        id = input("Id da inspeção: ").strip()
        apto = input("Captidão do carro: ").strip()
        resultado = input("Resultado da inspeção: ").strip()
        return {
            "placa": placa,
            "id": id,
            "apto": apto,
            "resultado": resultado,
        }        
    
    def validar_placa(self, placa):
        for carro in ControladorAssocCarroInspecao.lista_carros:
            if(carro.placa == placa):
                return True
            return False
    
    def request_criar_associacao(self):
        dados_associacao = self.pegar_dados
        ControladorAssocCarroInspecao.criar_associacao(dados_associacao["placa"], dados_associacao["id"], dados_associacao["apto"], dados_associacao["resultado"],)
        return

    #ainda vou fazer o listar e excluir
      
            


