class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # GETTER
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()


if __name__ == '__main__':
    p1 = Produto('Camisa', 120)
    p2 = Produto('Notebook', 'R$6900')

    p1.desconto(10)
    p2.desconto(10)

    print(p1.preco)
    print(p2.preco)

    print(p1.nome)
    print(p2.nome)
