"""
Associação - USA | Agregação - Tem | Composição - É dono | Herança - é
"""

from classes import *

p1 = Pessoa('Olivia', 25)
c1 = Cliente('Pedro', 29)
a1 = Aluno('Juliana', 25)
vip = ClienteVip('Marcia', 45, 'Lisboa')

c1.comprar()
a1.estudar()
vip.falar()