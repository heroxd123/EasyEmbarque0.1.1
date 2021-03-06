import PySimpleGUI as sg
from pessoa import Pessoa

class Tela_Pessoa:
    #       format='%d/%m/%Y'

    def __init__(self):
        layout = [
            [sg.Text('Rg:', size=(15, 0)), sg.Input(size=(10, 0),key='rg')],
            [sg.Text('Nome:', size=(15, 0)), sg.Input(size=(45, 0),key='nome')],
            [sg.Text('*A data deve ter a seguinte estrutura (DD/MM/AAAA)')],
            [sg.Text('Dt. Nascimento:', size=(15, 0)), sg.CalendarButton('Selecionar', format='%d/%m/%Y', size=(20, 0)
             , target='data_nascimento', key='calendario'), sg.Input('DD/MM/AAAA', size=(15, 0), key='data_nascimento')],
            [sg.Text('Sexo:', size=(15, 0)), sg.Combo(['Masculino', 'Feminino'], key='sexo')],
            [sg.Text('Telefone:', size=(15, 0)), sg.Input(size=(20, 0), key='telefone')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]

        ]

        janela = sg.Window("Dados Pessoais").layout(layout)
        self.button, self.values = janela.Read()

    def cadastrar_pessoa(self):
        rg = self.values['rg']
        nome = self.values['nome']
        data_nascimento = self.values['data_nascimento']
        sexo = self.values['sexo']
        telefone = self.values['telefone']
        pessoa = Pessoa(rg, nome, data_nascimento, sexo, telefone)
        pessoa.db_regitrar_pessoa()


tela = Tela_Pessoa()
tela.cadastrar_pessoa()
