import sqlite3


class Pessoa:
    def __init__(self, rg, nome, data_nascimento, sexo, telefone):
        self._rg = rg
        self._nome = nome.title()
        self._data_nascimento = data_nascimento
        self._sexo = sexo
        self.telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def calcula_idade(self):
        ano_atual = 2021
        ano_n = int(self._data_nascimento[6:10])
        idade = ano_atual - ano_n
        print("A idade do {} e {}".format(self.nome, idade))

    def db_regitrar_pessoa(self):
        banco = sqlite3.connect('pessoa.db')
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO pessoa VALUES('"+self._rg+"','"+self._nome+"','"+ self._data_nascimento+"','"+self._sexo+"','"+ self._telefone+"')")
        banco.commit()
        print("Deu bom jacaré")
