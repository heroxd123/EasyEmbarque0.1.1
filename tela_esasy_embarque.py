import PySimpleGUI as sg


class Tela_Pessoa:
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(10,0)), sg.Input(size=(40,0))],
            [sg.Text('A data dele ter a seguinte estrutura: (DD/MM/AAAA)')],
            [sg.Text('Data de Nascimento',size=(10,0)), sg.Input(size=(15,0))],
            [sg.Text('Sexo'),sg.Combo(['Masculino', 'Feminino'],key='sexo')],
            [sg.Button('Enviar')]
        ]
        janela = sg.Window("Dados Pessoais").layout(layout)

        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = Tela_Pessoa()
tela.Iniciar()


