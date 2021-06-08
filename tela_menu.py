import PySimpleGUI as sg

class Tela_Menu:

    def __init__(self):
        layout = [
        [sg.Text('Selecionar Opção'), sg.Input(key="campo")],
        [sg.Text('broca'), sg.Input('pao com feijao', key='larica')],
        [sg.Button('Enviar')]
        ]
        janela = sg.Window("Menu").layout(layout)

        self.button, self.values = janela.Read()

tela = Tela_Menu()