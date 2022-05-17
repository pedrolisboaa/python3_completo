"""
Estrutura de repetição FOR
"""

nome_completo = 'Olivia Oliviera Lisboa'
for i in nome_completo:
    print(i)


contator = 0
for i in range(100):
    contator += i

print(contator)
lista_de_100 = list(range(100))
print(sum(lista_de_100))

print('For com STEP')
for i in range(0, 100, 10):
    print(i)

print(list(range(0, 100, 10)))

vogais = ['a', 'e', 'i', 'o', 'u']
nome = 'pedro henrique do nascimento lisboa'
novo_nome = ''
for i in nome:
    if i in vogais:
        novo_nome += i.upper()
    else:
        novo_nome += i

print(nome)
print(novo_nome)