import PySimpleGUI as sg
from representante import Representante

class Tela_Representante:
    #       format='%d/%m/%Y'

    def __init__(self):
        sg.theme('Light Brown 1')
        layout = [
            [sg.Text('Código:', size=(15, 0)), sg.Input(size=(5, 0), key='codigo')],
            [sg.Text('Rg:', size=(15, 0)), sg.Input(size=(10, 0),key='rg')],
            [sg.Text('Nome:', size=(15, 0)), sg.Input(size=(45, 0),key='nome')],
            [sg.Text('*A data deve ter a seguinte estrutura (DD/MM/AAAA)')],
            [sg.Text('Dt. Nascimento:', size=(15, 0)), sg.CalendarButton('Selecionar', format='%d/%m/%Y', size=(20, 0)
             , target='data_nascimento', key='calendario'), sg.Input('DD/MM/AAAA', size=(15, 0), key='data_nascimento')],
            [sg.Text('Sexo:', size=(15, 0)), sg.Combo(['Masculino', 'Feminino'], key='sexo')],
            [sg.Text('Telefone:', size=(15, 0)), sg.Input(size=(20, 0), key='telefone')],
            [sg.Text('Comissao:', size=(15, 0)), sg.Combo([5,6,7,8,9], key='comissao'), sg.Text('%')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]

        ]

        janela = sg.Window("06062021 Cadastrar Representante").layout(layout)
        self.button, self.values = janela.Read()

    def cadastrar_representante(self):
        codigo = self.values['codigo']
        rg = self.values['rg']
        nome = self.values['nome']
        data_nascimento = self.values['data_nascimento']
        sexo = self.values['sexo']
        telefone = self.values['telefone']
        comissao = self.values['comissao']
        representante = Representante(codigo, rg, nome, data_nascimento, sexo, telefone, comissao)
        representante.db_regitrar_representante()


tela = Tela_Representante()
tela.cadastrar_representante()
