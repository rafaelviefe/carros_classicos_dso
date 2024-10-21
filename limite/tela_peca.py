class TelaPeca:
    def tela_opcoes(self):
        opcao = -1  
        while opcao not in [0, 1, 2, 3, 4, 0]:
            try:
                print("-------- PEÇAS ----------")
                print("Escolha a opção")
                print("1 - Incluir Peça")
                print("2 - Listar Peças")
                print("3 - Excluir Peça")
                print("0 - Retornar")

                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        return opcao

    def pega_dados_motor(self):
        num_motor = input("Número do Motor: ").strip()
        while not num_motor:
            print("Número do Motor inválido! O campo não pode ser vazio.")
            num_motor = input("Número do Motor: ").strip()

        input_valido = False
        while not input_valido:
            try:
                potencia = float(input("Potência: ").strip())
                input_valido = True
            except ValueError:
                print("Potência inválida! Por favor, insira um número decimal.")

        input_valido = False
        while not input_valido:
            try:
                cilindrada = float(input("Cilindrada: ").strip())
                input_valido = True
            except ValueError:
                print("Cilindrada inválida! Por favor, insira um número decimal.")

        tipo_combustivel = input("Tipo de Combustível: ").strip()
        while not tipo_combustivel:
            print("Tipo de combustível inválido! O campo não pode ser vazio.")
            tipo_combustivel = input("Tipo de Combustível: ").strip()

        input_valido = False
        while not input_valido:
            try:
                num_cilindros = int(input("Número de Cilindros: ").strip())
                input_valido = True
            except ValueError:
                print("Número de cilindros inválido! Por favor, insira um número inteiro.")

        input_valido = False
        while not input_valido:
            try:
                torque = float(input("Torque: ").strip())
                input_valido = True
            except ValueError:
                print("Torque inválido! Por favor, insira um número decimal.")

        return {
            "num_motor": num_motor,
            "potencia": potencia,
            "cilindrada": cilindrada,
            "tipo_combustivel": tipo_combustivel,
            "num_cilindros": num_cilindros,
            "torque": torque
        }

    def pega_dados_roda(self):
        num_serie = input("Número de Série: ").strip()
        while not num_serie:
            print("Número de Série inválido! O campo não pode ser vazio.")
            num_serie = input("Número de Série: ").strip()

        input_valido = False
        while not input_valido:
            try:
                largura = float(input("Largura: ").strip())
                input_valido = True
            except ValueError:
                print("Largura inválida! Por favor, insira um número decimal.")

        input_valido = False
        while not input_valido:
            try:
                perfil = float(input("Perfil: ").strip())
                input_valido = True
            except ValueError:
                print("Perfil inválido! Por favor, insira um número decimal.")

        tipo = input("Tipo: ").strip()
        while not tipo:
            print("Tipo inválido! O campo não pode ser vazio.")
            tipo = input("Tipo: ").strip()

        input_valido = False
        while not input_valido:
            try:
                diametro_aro = int(input("Diâmetro do Aro: ").strip())
                input_valido = True
            except ValueError:
                print("Diâmetro do aro inválido! Por favor, insira um número inteiro.")

        input_valido = False
        while not input_valido:
            try:
                indice_carga = int(input("Índice de Carga: ").strip())
                input_valido = True
            except ValueError:
                print("Índice de carga inválido! Por favor, insira um número inteiro.")

        indice_velocidade = input("Índice de Velocidade: ").strip()
        while not indice_velocidade:
            print("Índice de velocidade inválido! O campo não pode ser vazio.")
            indice_velocidade = input("Índice de Velocidade: ").strip()

        return {
            "num_serie": num_serie,
            "largura": largura,
            "perfil": perfil,
            "tipo": tipo,
            "diametro_aro": diametro_aro,
            "indice_carga": indice_carga,
            "indice_velocidade": indice_velocidade
        }

    def pega_dados_pintura(self):
        codigo_cor = input("Código da Cor: ").strip()
        while not codigo_cor:
            print("Código da cor inválido! O campo não pode ser vazio.")
            codigo_cor = input("Código da Cor: ").strip()

        cor = input("Cor: ").strip()
        while not cor:
            print("Cor inválida! O campo não pode ser vazio.")
            cor = input("Cor: ").strip()

        tipo = input("Tipo de Pintura: ").strip()
        while not tipo:
            print("Tipo inválido! O campo não pode ser vazio.")
            tipo = input("Tipo de Pintura: ").strip()

        input_valido = False
        while not input_valido:
            try:
                camadas = int(input("Número de Camadas: ").strip())
                input_valido = True
            except ValueError:
                print("Número de camadas inválido! Por favor, insira um número inteiro.")

        return {
            "codigo_cor": codigo_cor,
            "cor": cor,
            "tipo": tipo,
            "camadas": camadas
        }
    
    def mostra_motor(self, dados_motor):
        print("Número do Motor: ", dados_motor["num_motor"])
        print("Potência: ", dados_motor["potencia"])
        print("Cilindrada: ", dados_motor["cilindrada"])
        print("Tipo de Combustível: ", dados_motor["tipo_combustivel"])
        print("Número de Cilindros: ", dados_motor["num_cilindros"])
        print("Torque: ", dados_motor["torque"])
        print("\n")

    def mostra_roda(self, dados_roda):
        print("Número de Série: ", dados_roda["num_serie"])
        print("Largura: ", dados_roda["largura"])
        print("Perfil: ", dados_roda["perfil"])
        print("Tipo: ", dados_roda["tipo"])
        print("Diâmetro do Aro: ", dados_roda["diametro_aro"])
        print("Índice de Carga: ", dados_roda["indice_carga"])
        print("Índice de Velocidade: ", dados_roda["indice_velocidade"])
        print("\n")

    def mostra_pintura(self, dados_pintura):
        print("Código da Cor: ", dados_pintura["codigo_cor"])
        print("Cor: ", dados_pintura["cor"])
        print("Tipo de Pintura: ", dados_pintura["tipo"])
        print("Número de Camadas: ", dados_pintura["camadas"])
        print("\n")

    def seleciona_peca(self):
        print("Selecione o tipo de peça:")
        print("1 - Motor")
        print("2 - Roda")
        print("3 - Pintura")

        tipo_peca = -1
        while tipo_peca not in [1, 2, 3]:
            try:
                tipo_peca = int(input("Escolha o tipo de peça: "))
                if tipo_peca not in [1, 2, 3]:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")

        if tipo_peca == 1:
            identificador = input("Informe o número do motor: ").strip()
            while not identificador:
                print("Número do motor inválido! O campo não pode ser vazio.")
                identificador = input("Informe o número do motor: ").strip()
            tipo = "motor"

        elif tipo_peca == 2:
            identificador = input("Informe o número de série da roda: ").strip()
            while not identificador:
                print("Número de série inválido! O campo não pode ser vazio.")
                identificador = input("Informe o número de série da roda: ").strip()
            tipo = "roda"

        elif tipo_peca == 3:
            identificador = input("Informe o código da cor da pintura: ").strip()
            while not identificador:
                print("Código da cor inválido! O campo não pode ser vazio.")
                identificador = input("Informe o código da cor da pintura: ").strip()
            tipo = "pintura"

        return tipo, identificador

    def mostra_mensagem(self, msg):
        print(msg)
