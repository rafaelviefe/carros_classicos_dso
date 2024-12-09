import PySimpleGUI as sg

class TelaAssocCarroInspecao:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Gerenciamento de Inspeções', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Incluir Inspeção', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Listar Inspeções', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Excluir Inspeção', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Obter Relatório', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Retornar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos - Inspeções',
            layout,
            element_justification='center',
            size=(800, 400)
        )

        button, _ = self.open()
        opcao = {
            'Incluir Inspeção': 1,
            'Listar Inspeções': 2,
            'Excluir Inspeção': 3,
            'Obter Relatório': 4,
            'Retornar': 0,
        }.get(button, 0)
        self.close()
        return opcao

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
            [sg.Text('Digite o ID da inspeção que deseja selecionar:', font=("Helvetica", 16), pad=(0, 20))],
            [sg.InputText('', key='id_inspecao', size=(10, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
            sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Informe o ID da inspeção', layout, element_justification='center', size=(600, 200))

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                id_inspecao = int(values['id_inspecao'].strip())
                if id_inspecao >= 0:
                    self.close()
                    return id_inspecao
                else:
                    raise ValueError
            except ValueError:
                self.mostra_mensagem("ID inválido! Por favor, insira um número inteiro positivo.")

    def pega_pecas_esperadas(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Verificação de peças esperadas', font=("Helvetica", 25), justification='center', pad=(0, 20))],
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
                    "motor": num_motor,
                    "roda": num_serie,
                    "pintura": codigo_cor,
                }
            else:
                self.mostra_mensagem("Todos os campos são obrigatórios! Preencha corretamente.")

    def mostra_inspecoes(self, lista_inspecoes):
        sg.theme('BlueMono')

        if not lista_inspecoes:
            self.mostra_mensagem("Nenhuma inspeção encontrada.")
            return

        headers = ['ID', 'Apto', 'Resultado']
        data = [
            [inspecao['id'], 'Sim' if inspecao['apto'] else 'Não', inspecao['resultado'].capitalize()]
            for inspecao in lista_inspecoes
        ]

        layout = [
            [sg.Text('Inspeções Encontradas', font=("Helvetica", 25), justification='center', pad=(0, 20))],
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

        window = sg.Window('Lista de Inspeções', layout, size=(800, 400), element_justification='center')
        while True:
            event, _ = window.read()
            if event in (None, 'Fechar'):
                break
        window.close()

    def mostra_inconstancias(self, pecas_diferentes):
        sg.theme('BlueMono')

        if not pecas_diferentes:
            self.mostra_mensagem("Nenhuma diferença encontrada nas peças.")
            return

        data = [
            [peca.capitalize(), valores[0], valores[1]]
            for peca, valores in pecas_diferentes.items()
        ]

        layout = [
            [sg.Text('Peças Diferentes Encontradas', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Table(
                values=data,
                headings=['Peça', 'Atual', 'Esperado'],
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

        window = sg.Window('Inconsistências nas Peças', layout, size=(800, 400), element_justification='center')
        while True:
            event, _ = window.read()
            if event in (None, 'Fechar'):
                break
        window.close()

    def obtem_data(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Digite a Data da Inspeção', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('Mês (1-12):', size=(20, 1)), sg.InputText('', key='mes', size=(5, 1))],
            [sg.Text('Ano:', size=(20, 1)), sg.InputText('', key='ano', size=(5, 1))],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Inspeção - Data',
            layout,
            element_justification='center',
            size=(500, 300)
        )

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                mes = int(values['mes'].strip())
                ano = int(values['ano'].strip())

                if mes < 1 or mes > 12:
                    raise ValueError("O mês deve estar entre 1 e 12.")
                if ano < 0:
                    raise ValueError("O ano deve ser um valor positivo.")

                data_formatada = f"{mes:02d}-{ano}"
                self.close()
                return data_formatada
            except ValueError as e:
                self.mostra_mensagem(f"Entrada inválida: {str(e)}")

    def mostra_relatorio(self, relatorio):
        sg.theme('BlueMono')

        data = relatorio["data"]
        total = relatorio["total"]

        status_layout = [
            [sg.Text(f"STATUS - Data: {data}", font=("Helvetica", 16), pad=(0, 10))],
            [sg.Text(f"  - Aprovadas: {relatorio['aprovacao']['porcentagem']:.2f}% "
                     f"({relatorio['aprovacao']['num']}/{total})", font=("Helvetica", 13))],
            [sg.Text(f"  - Pendentes: {relatorio['pendencia']['porcentagem']:.2f}% "
                     f"({relatorio['pendencia']['num']}/{total})", font=("Helvetica", 13))],
            [sg.Text(f"  - Reprovadas: {relatorio['reprovacao']['porcentagem']:.2f}% "
                     f"({relatorio['reprovacao']['num']}/{total})", font=("Helvetica", 13))],
        ]

        ranking_layout = [
            [sg.Text("Ranking dos Carros", font=("Helvetica", 18, "bold"), pad=(0, 10))],
            [sg.Text("MAIS INSPEÇÕES", font=("Helvetica", 14))],
        ] + [
            [sg.Text(f"  {i + 1}° - VIN: {carro['vin']} com {carro['qtd']} inspeções", font=("Helvetica", 12))]
            for i, carro in enumerate(relatorio["carros_por_inspecao"])
        ] + [
            [sg.Text("\nMAIOR PERCENTUAL DE IRREGULARES:", font=("Helvetica", 14))],
        ] + [
            [sg.Text(f"  {i + 1}° - VIN: {carro['vin']} com {carro['porcentagem']:.2f}% irregularidade", font=("Helvetica", 12))]
            for i, carro in enumerate(relatorio["carros_por_reprovacao"])
        ] + [
            [sg.Text("\nMAIOR PERCENTUAL DE APROVAÇÃO:", font=("Helvetica", 14))],
        ] + [
            [sg.Text(f"  {i + 1}° - VIN: {carro['vin']} com {carro['porcentagem']:.2f}% aprovação", font=("Helvetica", 12))]
            for i, carro in enumerate(relatorio["carros_por_aprovacao"])
        ]

        layout = [
            [sg.Text('Relatório de Inspeções', font=("Helvetica", 20, "bold"), justification='center', pad=(0, 20))],
            [sg.Column(status_layout, pad=(10, 10), element_justification='center')],
            [sg.Column(ranking_layout, pad=(10, 10), element_justification='center')],
            [sg.Button('Fechar', size=(15, 1), button_color=('white', '#FF4C4C'), pad=(0, 20))]
        ]

        self.__window = sg.Window(
            'Relatório de Inspeções',
            layout,
            size=(800, 850),
            element_justification='center',
            modal=True
        )

        while True:
            event, _ = self.__window.read()
            if event in (None, 'Fechar'):
                break

        self.__window.close()

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