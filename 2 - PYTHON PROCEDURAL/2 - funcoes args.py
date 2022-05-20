"""
Funções com *args e **kwargs
"""


def somando_varios(*args):
    return sum(args)


def informando_dados(**kwargs):
   nome = kwargs.get('nome')
   idade = kwargs.get('idade')

   print(f'O {nome} tem {idade} anos.')


teste = somando_varios(5, 3, 3, 5, 6)
lista = list(range(0, 100))
somar_toda_lista = somando_varios(*lista)

print(teste)
print(somar_toda_lista)
informando_dados(nome='Pedro', idade=28)