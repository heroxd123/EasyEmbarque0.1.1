import PySimpleGUI as sg

class Tela_Menu:

    def __init__(self):
        layout = [
        [sg.Text('Selecionar Opção')],
        [sg.Button('Enviar')]
        ]
        janela = sg.Window("Menu").layout(layout)

        self.button, self.values = janela.Read()

tela = Tela_Menu()