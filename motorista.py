from pessoa import Pessoa


class Motorista(Pessoa):
    def __init__(self, rg, nome, data_nascimento, sexo, telefone, cnh, apelido):
        super().__init__(rg, nome, data_nascimento, sexo, telefone)
        self.cnh = cnh
        self.apelido = apelido

    # Validando se a CNH do Motorista está de acordo
    def verificar_cnh(self):
        if self.cnh == "A":
            print("O Motorista {} não pode dirigir por possuir cnh tipo {}".format(self.apelido, self.cnh))
        else:
            print("O Motorista {} pode dirigir!".format(self.apelido))
            return
