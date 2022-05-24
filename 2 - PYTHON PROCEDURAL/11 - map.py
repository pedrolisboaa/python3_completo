from dados import pessoas, lista, produtos

# Sem lambda
def teste(x):
    return x * 2


nova_lista = map(teste, lista)
for _ in nova_lista:
    print(_)

# Com lambda e map
lista_lambda = map(lambda x: x * 2, lista)
print(list(lista_lambda))

# Com list
lista_com_list = [x * 2 for x in lista]
print(lista_com_list)

# Agora com dicionarios é melhor com MAP
precos = map(lambda p: round(p['preco'] + (5 / 100), 2), produtos)
for _ in precos:
    print(_)


nomes = map(lambda nome: nome['nome'].upper(), pessoas)
for _ in nomes:
    print(_)
