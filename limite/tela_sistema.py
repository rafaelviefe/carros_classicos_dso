import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, _ = self.__window.Read()
        opcao = {
            'Clientes': 1,
            'Carros': 2,
            'Inspeções': 3,
            'Peças': 4,
            'Transferências': 5,
            'Finalizar': 0,
            None: 0,  # Para tratar o caso de fechamento da janela
        }.get(button, 0)
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.theme('BlueMono')  # Tema moderno e atrativo

        layout = [
            [sg.Text('Concessionária Clássica', font=("Helvetica", 30), justification='center', expand_x=True)],
            [sg.Text('Escolha sua opção abaixo:', font=("Helvetica", 14), pad=(0, 20))],
            [sg.Button('Clientes', size=(15, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Carros', size=(15, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Inspeções', size=(15, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Peças', size=(15, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Transferências', size=(15, 2), button_color=('white', '#2a9df4'))],
            [sg.Button('Finalizar', size=(15, 2), button_color=('white', '#FF4C4C'))],
        ]

        self.__window = sg.Window(
            'Sistema de Carros Clássicos',
            layout,
            element_justification='center',  # Centraliza os elementos
            size=(600, 400),
        )
