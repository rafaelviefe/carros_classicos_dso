import PySimpleGUI as sg

class TelaTransferencia:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Gerenciamento de Transferências', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Incluir Transferência', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Alterar Transferência', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Listar Transferências', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Excluir Transferência', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Retornar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos - Transferências',
            layout,
            element_justification='center',
            size=(800, 400)
        )

        button, _ = self.open()
        opcao = {
            'Incluir Transferência': 1,
            'Alterar Transferência': 2,
            'Listar Transferências': 3,
            'Excluir Transferência': 4,
            'Retornar': 0,
        }.get(button, 0)
        self.close()
        return opcao

    def pega_dados_transferencia(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Cadastro de Transferência', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('VIN do carro:', size=(20, 1)), sg.InputText('', key='vin_carro')],
            [sg.Text('Tipo de transferência:', size=(20, 1)), 
             sg.Combo(['compra', 'venda'], key='tipo', readonly=True)],
            [sg.Text('Documento da pessoa:', size=(20, 1)), sg.InputText('', key='documento')],
            [sg.Text('Valor da transferência (R$):', size=(20, 1)), sg.InputText('', key='valor')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Cadastro de Transferência',
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
                vin_carro = values['vin_carro'].strip()
                tipo = values['tipo']
                documento = values['documento'].strip()
                valor = float(values['valor'].strip())

                if not vin_carro or not tipo or not documento or valor <= 0:
                    raise ValueError("Todos os campos devem ser preenchidos corretamente.")

                self.close()
                return {
                    "vin_carro": vin_carro,
                    "tipo": tipo,
                    "documento_pessoa": documento,
                    "valor": valor,
                }
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Verifique os campos e tente novamente.")

    def pega_alteracoes_transferencia(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Alterar Transferência', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('Novo valor da transferência (R$):', size=(25, 1)), sg.InputText('', key='valor')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Alteração de Transferência',
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
                valor = float(values['valor'].strip())
                if valor <= 0:
                    raise ValueError("O valor deve ser maior que zero.")
                self.close()
                return {"valor": valor}
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Insira um valor válido.")
    
    def pega_vin(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite o VIN do carro em questão:', font=("Helvetica", 16), pad=(0, 20))],
            [sg.InputText('', key='vin_carro', size=(30, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
            sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Informe o VIN', layout, element_justification='center', size=(600, 200))

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
        
    def pega_id(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite o ID da transferência que deseja selecionar:', font=("Helvetica", 16), pad=(0, 20))],
            [sg.InputText('', key='id_transferencia', size=(10, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
            sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Informe o ID da Transferência', layout, element_justification='center', size=(600, 200))

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                id_transferencia = int(values['id_transferencia'].strip())
                if id_transferencia >= 0:
                    self.close()
                    return id_transferencia
                else:
                    raise ValueError
            except ValueError:
                self.mostra_mensagem("ID inválido! Por favor, insira um número inteiro positivo.")
    
    def mostra_transferencias(self, transferencias):
        sg.theme('BlueMono')

        if not transferencias:
            self.mostra_mensagem("Nenhuma transferência encontrada.")
            return

        headers = ['ID', 'VIN do Carro', 'Tipo', 'Documento', 'Valor']
        data = [
            [t['id'], t['vin_carro'], t['tipo'].capitalize(), t['documento_pessoa'], f"R$ {t['valor']:.2f}"]
            for t in transferencias
        ]

        layout = [
            [sg.Text('Lista de Transferências', font=("Helvetica", 25), justification='center', pad=(0, 20))],
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

        window = sg.Window('Transferências', layout, size=(1000, 600), element_justification='center')
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