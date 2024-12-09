import re
import PySimpleGUI as sg

class TelaPessoa:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Gerenciamento de Pessoas', font=("Helvetica", 28, "bold"), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 16), justification='center', pad=(0, 20))],
            [sg.Button('Incluir Pessoa', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Alterar Pessoa', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Listar Pessoas', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Excluir Pessoa', size=(20, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Retornar', size=(20, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos - Pessoas',
            layout,
            element_justification='center',
            size=(800, 400)
        )

        button, _ = self.open()
        opcao = {
            'Incluir Pessoa': 1,
            'Alterar Pessoa': 2,
            'Listar Pessoas': 3,
            'Excluir Pessoa': 4,
            'Retornar': 0,
        }.get(button, 0)
        self.close()
        return opcao

    def pega_dados_pessoa(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Cadastro de Pessoa', font=("Helvetica", 25), justification='center', pad=(0, 20))],
            [sg.Text('Nome:', size=(20, 1)), sg.InputText('', key='nome')],
            [sg.Text('Documento (CPF ou CNPJ):', size=(20, 1)), sg.InputText('', key='documento')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Cadastro de Pessoa',
            layout,
            element_justification='center',
            size=(600, 300)
        )

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            nome = values['nome'].strip()
            documento = values['documento'].strip()

            if not nome:
                self.mostra_mensagem("Nome inválido! O nome não pode ser vazio.")
            elif not self.validar_documento(documento):
                self.mostra_mensagem("Documento inválido! Insira um CPF ou CNPJ válido.")
            else:
                self.close()
                return {"nome": nome, "documento": documento}

    # Remove todos os não digitos do documento e decide entre cpf e cnpj
    def validar_documento(self, documento: str) -> bool:
        documento = re.sub(r'\D', '', documento)
        if len(documento) == 11:
            return self.validar_cpf(documento)
        elif len(documento) == 14:
            return self.validar_cnpj(documento)
        else:
            return False

    # Algorítimo padrão para validar cpf
    def validar_cpf(self, cpf: str) -> bool:
        if cpf == cpf[0] * len(cpf):
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return cpf[-2:] == f"{digito1}{digito2}"

    # Algorítimo padrão para validar cnpj
    def validar_cnpj(self, cnpj: str) -> bool:
        if cnpj == cnpj[0] * len(cnpj):
            return False

        def calcula_digito(cnpj, peso):
            soma = sum(int(cnpj[i]) * peso[i] for i in range(len(peso)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        digito1 = calcula_digito(cnpj[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

        digito2 = calcula_digito(cnpj[:13], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

        return cnpj[-2:] == f"{digito1}{digito2}"

    def pega_novo_nome(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Alterar Nome', font=("Helvetica", 20), justification='center', pad=(0, 20))],
            [sg.Text('Novo nome:', size=(20, 1)), sg.InputText('', key='novo_nome')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Alterar Nome', layout, element_justification='center', size=(500, 200))

        while True:
            button, values = self.__window.read()
            if button in (None, 'Cancelar'):
                self.__window.close()
                return None

            novo_nome = values['novo_nome'].strip()
            if novo_nome:
                self.__window.close()
                return novo_nome
            else:
                self.mostra_mensagem("Nome inválido! O nome não pode ser vazio.")

    def mostra_pessoas(self, lista_pessoas):
        sg.theme('BlueMono')

        if not lista_pessoas:
            self.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return

        layout = [[sg.Text("Lista de Pessoas Cadastradas", font=("Helvetica", 20), justification='center', pad=(0, 20))]]
        
        for pessoa in lista_pessoas:
            pessoa_section = [
                [sg.Text(f"Nome: {pessoa['nome']}", font=("Helvetica", 16), pad=(0, 5))],
                [sg.Text(f"Documento: {pessoa['documento']}", font=("Helvetica", 14), pad=(0, 5))]
            ]
            
            if pessoa["carros"]:
                pessoa_section.append([sg.Text("Carros:", font=("Helvetica", 14, "bold"), pad=(0, 5))])
                for carro in pessoa["carros"]:
                    pessoa_section.extend([
                        [sg.Text(f"VIN: {carro['vin']} - Modelo: {carro['modelo']} - Ano: {carro['ano']}", font=("Helvetica", 12))]
                    ])
            else:
                pessoa_section.append([sg.Text("Sem carros cadastrados.", font=("Helvetica", 12), pad=(0, 5))])
            
            pessoa_section.append([sg.HorizontalSeparator()])
            layout.extend(pessoa_section)

        layout.append([sg.Button("Fechar", size=(15, 1), button_color=("white", "#2a9df4"))])

        self.__window = sg.Window(
            "Pessoas Cadastradas",
            layout,
            size=(800, 600),
            element_justification='center',
            modal=True,
            resizable=True,
        )

        while True:
            event, _ = self.__window.read()
            if event in (None, "Fechar"):
                break

        self.close()

    def seleciona_pessoa(self):
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Selecionar Pessoa', font=("Helvetica", 20), justification='center', pad=(0, 20))],
            [sg.Text('Documento do cliente:', size=(20, 1)), sg.InputText('', key='documento')],
            [sg.Button('Confirmar', size=(15, 1), button_color=('white', '#2a9df4')),
             sg.Button('Cancelar', size=(15, 1), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window('Selecionar Pessoa', layout, element_justification='center', size=(500, 200))

        while True:
            button, values = self.__window.read()
            if button in (None, 'Cancelar'):
                self.__window.close()
                return None

            documento = values['documento'].strip()
            if documento:
                self.__window.close()
                return documento
            else:
                self.mostra_mensagem("Documento inválido! O documento não pode ser vazio.")

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