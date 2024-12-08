import PySimpleGUI as sg

class TelaCarroClassico:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Gerenciamento de Carros Clássicos', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Incluir Carro', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Alterar Carro', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Listar Carros', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Excluir Carro', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Trocar Peças', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Retornar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos',
            layout,
            element_justification='center',
            size=(800, 500)
        )

        button, _ = self.open()
        opcao = {
            'Incluir Carro': 1,
            'Alterar Carro': 2,
            'Listar Carros': 3,
            'Excluir Carro': 4,
            'Trocar Peças': 5,
            'Retornar': 0,
        }.get(button, 0)
        self.close()
        return opcao
    
    def pega_dados_carro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Cadastro de Carro Clássico', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('VIN:', size=(20, 1)), sg.InputText('', key='vin')],
            [sg.Text('Placa:', size=(20, 1)), sg.InputText('', key='placa')],
            [sg.Text('Modelo:', size=(20, 1)), sg.InputText('', key='modelo')],
            [sg.Text('Ano:', size=(20, 1)), sg.InputText('', key='ano')],
            [sg.Text('Quilometragem:', size=(20, 1)), sg.InputText('', key='quilometragem')],
            [sg.Text('Tipo de câmbio:', size=(20, 1)), sg.InputText('', key='cambio')],
            [sg.Text('Unidades existentes:', size=(20, 1)), sg.InputText('', key='unidades_existentes')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
            sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Cadastro de Carro Clássico',
            layout,
            element_justification='center',
            size=(600, 500)
        )

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                vin = values['vin'].strip()
                placa = values['placa'].strip()
                modelo = values['modelo'].strip()
                ano = int(values['ano'].strip())
                quilometragem = float(values['quilometragem'].strip())
                cambio = values['cambio'].strip()
                unidades_existentes = int(values['unidades_existentes'].strip())

                if not (vin and placa and modelo and cambio):
                    raise ValueError("Todos os campos devem ser preenchidos corretamente.")

                self.close()
                return {
                    "vin": vin,
                    "placa": placa,
                    "modelo": modelo,
                    "ano": ano,
                    "quilometragem": quilometragem,
                    "cambio": cambio,
                    "unidades_existentes": unidades_existentes,
                }
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Verifique os campos e tente novamente.")
    
    def pega_alteracoes_carro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Alterar Informações do Carro', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('Nova Placa:', size=(20, 1)), sg.InputText('', key='placa')],
            [sg.Text('Nova Quilometragem:', size=(20, 1)), sg.InputText('', key='quilometragem')],
            [sg.Text('Unidades Existentes:', size=(20, 1)), sg.InputText('', key='unidades_existentes')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Alteração de Carro',
            layout,
            element_justification='center',
            size=(600, 300)
        )

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                placa = values['placa'].strip()
                quilometragem = float(values['quilometragem'].strip())
                unidades_existentes = int(values['unidades_existentes'].strip())

                if not placa or quilometragem < 0 or unidades_existentes < 0:
                    raise ValueError("Todos os campos devem ser preenchidos corretamente.")

                self.close()
                return {
                    "placa": placa,
                    "quilometragem": quilometragem,
                    "unidades_existentes": unidades_existentes,
                }
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Verifique os campos e tente novamente.")

    def pega_pecas_carro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Cadastro de Peças do Carro', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('Número do Motor:', size=(20, 1)), sg.InputText('', key='num_motor')],
            [sg.Text('Número de Série da Roda:', size=(20, 1)), sg.InputText('', key='num_serie')],
            [sg.Text('Código da Pintura:', size=(20, 1)), sg.InputText('', key='codigo_cor')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Cadastro de Peças',
            layout,
            element_justification='center',
            size=(600, 300)
        )

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            num_motor = values['num_motor'].strip()
            num_serie = values['num_serie'].strip()
            codigo_cor = values['codigo_cor'].strip()

            if num_motor and num_serie and codigo_cor:
                self.close()
                return {
                    "num_motor": num_motor,
                    "num_serie": num_serie,
                    "codigo_cor": codigo_cor,
                }
            else:
                self.mostra_mensagem("Todos os campos são obrigatórios! Preencha corretamente.")

    def seleciona_carro(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Seleção de Carro', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Digite o VIN do carro que deseja selecionar:', font=("Helvetica", 16), pad=(0, 20))],
            [sg.InputText('', key='vin_carro', size=(30, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Seleção de Carro', layout, element_justification='center', size=(600, 250))

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            vin = values['vin_carro'].strip()
            if vin:
                self.close()
                return vin
            else:
                self.mostra_mensagem("VIN inválido! Por favor, insira um VIN válido.")

    def mostra_lista_carros(self, lista_carros):
        sg.theme('BlueMono')

        if not lista_carros:
            self.mostra_mensagem("Nenhum carro clássico encontrado.")
            return

        headers = ['VIN', 'Modelo', 'Ano', 'Unidades Existentes']
        data = [
            [carro['vin'], carro['modelo'], carro['ano'], carro['unidades_existentes']]
            for carro in lista_carros
        ]

        layout = [
            [sg.Text('Carros Clássicos', font=("Helvetica", 25), justification='center', pad=(0, 20))],
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
                expand_x=True,
                expand_y=True,
                key='-TABLE-'
            )],
            [sg.Button('Fechar', size=(15, 1), button_color=('white', '#2a9df4'))],
        ]

        window = sg.Window('Lista de Carros', layout, size=(1000, 600), element_justification='center')
        while True:
            event, _ = window.read()
            if event in (None, 'Fechar'):
                break
        window.close()

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
        self.__window.close()

    def open(self):
        button, values = self.__window.read()
        return button, values