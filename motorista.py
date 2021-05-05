from pessoa import Pessoa


class Motorista(Pessoa):
    def __init__(self, chn):
        self.cnh = "a"

    def verificar_cnh(self):
        if self.cnh == "a":
            print("O Motorista não pode dirigir")
        else:
            print("Não pode dirigir esse veículo")
            return
