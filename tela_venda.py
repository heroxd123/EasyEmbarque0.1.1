from pessoa import Pessoa
from evento import Evento
from excursao import Excursao
import PySimpleGUI as sg
class Tela_Venda:

    def __init__(self):
     sg.theme('Light Brown 1')
     radio_choices = ['Ingresso+Excursão', 'Excursão']
     layout = [
         [sg.Text("Informe seu Rg:", size =(11,0)), sg.Input(size=(6, 0), key='rg')],
         [sg.Text("Selecione a opção desejada")],
         [sg.Radio(text, 1)for text in radio_choices],
         [sg.Text("Selecione o evento que deseja realizar a compra", size=(18,0 )), sg.Combo(['Zuvuya', 'Universo Paralello', 'Boom Festival'], key='evento')],
         [sg.Text("Valor:", size=(4,0)), sg.Input(size=(5,0), key='valor')],
         [sg.Button("Finalizar Compra"), sg.Button("Cancelar")]
     ]

     janela = sg.Window("Realização da Compra").layout(layout)
     self.button, self.values = janela.Read()

tela = Tela_Venda()






