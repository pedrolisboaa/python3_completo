"""
Combination, Permutation e Product - Itertools
combinação  ordem nao importa
permuta ordem importa
Ambos não repetem valores únicos
Produto - ordem importa  e repete valores únicos
"""
from itertools import combinations, permutations, product

# pessoas = ['Pedro', 'Luiz', 'Juliana', 'Olívia', 'Juliana', 'Marcelo']
# contador = 0
# for grupo in product(pessoas, repeat=6):
#     print(grupo)
#     contador += 1
#
# print(f'O total é {contador}')

mega_sena = list(range(1, 60))
contador_mega = 0
for jogo in combinations(mega_sena, 6):
    contador_mega += 1

print(f'Na mega-sena é possível realizar {contador_mega} combinações')