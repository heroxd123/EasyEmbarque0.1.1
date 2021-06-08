import PySimpleGUI as sg
from evento import Evento


class Tela_Evento:
    def __init__(self):
        layout = [
            [sg.Text('Nome do Evento', size=(15, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('Codigo do Evento', size=(15, 0)), sg.Input(size=(10, 0), key='id')],
            [sg.Text('Telefone:', size=(15, 0)), sg.Input(size=(15, 0), key='telefone')],
            [sg.Text('Data do evento', size=(15, 0)), sg.CalendarButton('Selecionar', format='%d/%m/%Y', size=(20, 0)
                                                                        , target='data', key='calendario'),
             sg.Input('DD/MM/AAAA', size=(15, 0), key='data')],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window('Dados do Evento').layout(layout)
        self.button, self.values = janela.Read()

    def cadastrar_evento(self):
        nome = self.values["nome_evento"]
        id = self.values["id"]
        telefone = self.values["telefone"]
        data = self.values["data_evento"]
        evento = Evento(id, data, nome, telefone, )
        evento.db_registrar_evento()


tela = Tela_Evento()
tela.cadastrar_evento()
