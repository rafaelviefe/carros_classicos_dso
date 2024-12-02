import PySimpleGUI as sg

class TelaPeca:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.open()
        opcao = {
            'Incluir Peça': 1,
            'Listar Peças': 2,
            'Excluir Peça': 3,
            'Retornar': 0,
        }.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Gerenciamento de Peças', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Incluir Peça', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Listar Peças', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Excluir Peça', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Retornar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos - Peças',
            layout,
            element_justification='center',
            size=(600, 400),
        )

    def pega_dados_generico(self, tipo_peca, campos):
        sg.theme('BlueMono')
        layout = [
            [sg.Text(f'{tipo_peca.title()} - Cadastro', font=("Helvetica", 25), justification='center', pad=(0, 20))]
        ]

        for campo, tipo in campos.items():
            layout.append([sg.Text(f"{campo}:", size=(20, 1)), sg.InputText('', key=campo)])

        layout.append([
            sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
            sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))
        ])

        self.__window = sg.Window(f'Cadastro de {tipo_peca.title()}', layout, element_justification='center', size=(600, 400))

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                dados = {}
                for campo, tipo in campos.items():
                    valor = values[campo].strip()
                    if tipo == "int":
                        dados[campo] = int(valor) if valor else None
                    elif tipo == "float":
                        dados[campo] = float(valor) if valor else None
                    else:
                        dados[campo] = valor
                self.close()
                return dados
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Verifique os campos e tente novamente.")

    def pega_dados_motor(self):
        campos_motor = {
            "num_motor": "str",
            "potencia": "float",
            "cilindrada": "float",
            "tipo_combustivel": "str",
            "num_cilindros": "int",
            "torque": "float"
        }
        return self.pega_dados_generico("Motor", campos_motor)

    def pega_dados_roda(self):
        campos_roda = {
            "num_serie": "str",
            "largura": "float",
            "perfil": "float",
            "tipo": "str",
            "diametro_aro": "int",
            "indice_carga": "int",
            "indice_velocidade": "str"
        }
        return self.pega_dados_generico("Roda", campos_roda)

    def pega_dados_pintura(self):
        campos_pintura = {
            "codigo_cor": "str",
            "cor": "str",
            "tipo": "str",
            "camadas": "int"
        }
        return self.pega_dados_generico("Pintura", campos_pintura)
    
    def mostra_lista_pecas(self, tipo_peca_plural, lista_pecas):
        sg.theme('BlueMono')

        if not lista_pecas:
            sg.popup("Nenhuma peça encontrada.", title="Erro")
            return

        headers = list(lista_pecas[0].keys())
        data = [list(item.values()) for item in lista_pecas]

        layout = [
            [sg.Text(f'Lista de {tipo_peca_plural.title()}', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Table(
                values=data,
                headings=headers,
                auto_size_columns=False,
                justification='center',
                num_rows=min(15, len(data)),
                background_color='#f0f8ff',
                alternating_row_color='#e6f2ff',
                text_color='#000',
                header_background_color='#007acc',
                header_text_color='#fff',
                font=("Helvetica", 12),
                key='-TABLE-',
                expand_x=True,
                expand_y=True
            )],
            [sg.Button('Fechar', size=(15, 1), button_color=('white', '#2a9df4'))],
        ]

        window = sg.Window(f'Lista de {tipo_peca_plural.title()}', layout, element_justification='center', size=(1000, 600))
        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break
        window.close()

    def seleciona_tipo(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Selecione o tipo de peça:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Motor', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Roda', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Pintura', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Cancelar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Seleção de Tipo de Peça', layout, size=(600, 400), element_justification='center')
        button, _ = self.open()

        tipos = {
            'Motor': "motor",
            'Roda': "roda",
            'Pintura': "pintura",
            'Cancelar': None,
        }
        self.close()
        return tipos.get(button)

    def peca_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- PECAS ----------', font=("Helvica", 25))],
        [sg.Text('Selecione o tipo de peça:', font=("Helvica", 15))],
        [sg.Radio('Motor', "RD1", key='1')],
        [sg.Radio('Roda', "RD1", key='2')],
        [sg.Radio('Pintura', "RD1", key='3')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Carros Classicos').Layout(layout)

    def seleciona_peca(self):
        tipo = self.seleciona_tipo()
        if not tipo:
            return None, None

        label = {
            "motor": "Informe o número do motor:",
            "roda": "Informe o número de série da roda:",
            "pintura": "Informe o código da cor da pintura:",
        }[tipo]

        sg.theme('BlueMono')
        layout = [
            [sg.Text(label, font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.InputText('', key='identificador', size=(30, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(f'Seleção de {tipo.title()}', layout, element_justification='center', size=(600, 300))
        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None, None

            identificador = values['identificador'].strip()
            if identificador:
                self.close()
                return tipo, identificador
            else:
                self.mostra_mensagem("O campo não pode estar vazio. Tente novamente.")

    def mostra_mensagem(self, msg):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Mensagem', font=("Helvetica", 20), justification='center', expand_x=True)],
            [sg.Text(msg, font=("Helvetica", 14), justification='center', pad=(0, 20))],
            [sg.Button('OK', size=(15, 1), button_color=('white', '#2a9df4'))],
        ]

        window = sg.Window('Mensagem', layout, element_justification='center', modal=True)
        window.read()
        window.close()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values