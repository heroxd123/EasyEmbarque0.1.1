class Excursao:
import sqlite3
    def __init__(self, data_saida, data_retorno, cidade_destino, cidade_origem, preco):
        self.data_saida = data_saida
        self.data_retorno = data_retorno
        self.cidade_destino = cidade_destino
        self.cidade_origem = cidade_origem
        self.preco = preco

    def registrar_excursao(self):
        banco = sqlite3.connect('excursão.db')
        cursor = banco.cursor
        cursor.execute (
            "INSERT INTO excursão VALUES('"+self.data_saida+"', '"+self.data_retorno+"', '"+self.cidade_destino+"', '"+self.cidade_origem+"', '"+self.preco+"')"
        )