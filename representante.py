import Pessoa

class Representante(Pessoa):
    def __init__(self, rg, nome, data_nascimento, sexo, telefone, codigo, comissao):
        super().__init__(rg, nome, data_nascimento, sexo, telefone)
        self.__codigo = codigo
        self.__comissao = comissao

