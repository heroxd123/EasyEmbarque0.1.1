import Excursao


class Evento(Excursao):
    def __del__(self, data, ingresso):
        self.data = "20/11/2019"