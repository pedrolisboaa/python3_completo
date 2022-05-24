from functools import reduce
from dados import pessoas, lista, produtos

acumula = 0
for item in lista:
    acumula += item

print(acumula)

# Agora com reduce
soma_lista = reduce(lambda acumulador, item: item + acumula, lista, 0)
print(soma_lista)