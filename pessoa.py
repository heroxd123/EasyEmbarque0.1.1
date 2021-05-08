import sqlite3

class Pessoa:
    def __init__(self, nome, data_nascimento, sexo, telefone):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__telefone = telefone


    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento


    def calcula_idade(self):
        ano_atual = 2021
        ano_n = int(self.__data_nascimento[6:10])
        idade = ano_atual - ano_n
        print("A idade da {} e {}".format(self.nome,idade))