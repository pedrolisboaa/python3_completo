class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def mostrar_dados(self):
        for dado in self.endereco:
            print(f'{self.nome} - {self.idade}: {dado.cidade} {dado.estado}')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
