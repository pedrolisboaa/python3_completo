from datetime import datetime
class Pessoa:
    ANO_ATUAL = datetime.now().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = True
        self.falando = falando

    def esta_comendo(self, aliemento):
        if self.comendo:
            print(f'{self.nome} está comendo {aliemento}.')
        else:
            print(f'{self.nome} não está comendo')

    def comer(self):
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não pode parar pois não está comendo.')
            return

        self.comendo = False
        print(f'{self.nome} parou de comer.')

    def falar_nome(self):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo.')
            return
        print(f'Olá o meu nome é {self.nome}')

    def falar_ano_nascimento(self):
        ano_nascimento = self.ANO_ATUAL - self.idade
        print(f'Eu nascimento em {ano_nascimento}')

