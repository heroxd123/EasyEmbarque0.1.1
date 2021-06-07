from pessoa import Pessoa
import sqlite3

class Representante(Pessoa):


    def __init__(self, rg, nome, data_nascimento, sexo, telefone, codigo, comissao):
        super().__init__(rg, nome, data_nascimento, sexo, telefone)
        self.__codigo = codigo
        self.__comissao = comissao


    def db_regitrar_representante(self):
        banco = sqlite3.connect('representante.db')
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO representante VALUES(''"+self.__codigo+"','"+self._rg+"','"+self._nome+"','"+ self._data_nascimento+"','"+self._sexo+"','"+self._telefone+"','"+self.__comissao+"')")
        banco.commit()
        print("Simboraaaa Jacaré, kd minha vacina?")