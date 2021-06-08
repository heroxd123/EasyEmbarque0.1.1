import sqlite3

class Evento:
    def __init__(self, id, data, nome, preco_ingresso, lote):
        self._id = id
        self.data = data
        self.nome = nome
        self.preco_ingresso = preco_ingresso
        self.lote = lote

    def db_registrar_evento(self):
        banco = sqlite3.connect("evento.db")
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO evento VALUES("'+self._id+'", "'+self.nome+'", "'+self.preco_ingresso+'", "'+self.lote+'")"
        )
        banco.commit()
