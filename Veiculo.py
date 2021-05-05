class Veiculo:
    def __init__(self):
        self.cor = "Preto"
        self.capacidade_passageiros = 42
        self.velocidade = 0
        self.numero_rodas = 0

    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade
        print("Rodando as %s km/h" % self.velocidade)

    def parar(self):
        self.velocidade = 0
        print("Parrou geral")

    def buzinar(self):
        print("Bibiiiipp")


onibus = Veiculo()

onibus.cor = "Amarelo"
print(onibus.cor)
onibus.aumentar_velocidade(70)

