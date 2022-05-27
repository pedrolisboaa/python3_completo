class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if self.ligado:
            return
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return
        self.ligado = False
