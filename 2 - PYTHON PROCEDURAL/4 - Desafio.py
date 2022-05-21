lista_1 = [1, 2, 3, 4, 5, 6, 7]
lista_2 = [1, 2, 3, 4]
lista_ajuda = zip(lista_1, lista_2)
lista_soma = []

for n in lista_ajuda:
    lista_soma.append(n[0] + n[1])

print(lista_soma)

