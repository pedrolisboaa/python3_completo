from datetime import datetime
from random import randint


class Pessoa:
    ANO_ATUAL = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        ano_nascimento = self.ANO_ATUAL - self.idade
        print(f'Eu nasci e {ano_nascimento}')

    @classmethod
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ANO_ATUAL - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gerar_id():
        id = randint(1000, 9999)
        return id


