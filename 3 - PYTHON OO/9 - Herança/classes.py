class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Eu estou falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'Eu {self.nome} estou comprando.')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar()
        print(f'Eu {self.nome} {self.sobrenome} sou cliente VIP.')


class Aluno(Pessoa):
    def estudar(self):
        print(f'Eu {self.nome} estou estudando.')
