l1 = list(range(10))
l2 = [variavel ** 2 for variavel in l1]
print(l2)

# Exemplo 2
lista_nome = ['Pedro', 'Juliana', 'Olívia', 'Marcelo']
lista_nome_upper = [nome.upper() for nome in lista_nome]
print(lista_nome_upper)

# Exemplo 3
numeros_ate_100 = list(range(100))
lista_de_pares_ate_100 = [numero for numero in numeros_ate_100 if numero % 2 == 0]
lista_de_impares_ate_100 = [n for n in numeros_ate_100 if n % 2 != 0]
lista_de_divisiveis_por_5_8 = [n for n in numeros_ate_100 if n % 5 == 0 if n % 8 == 0]
print(lista_de_pares_ate_100)
print(lista_de_impares_ate_100)
print(lista_de_divisiveis_por_5_8)

# Exemplo 4
usando_replace = [nome.replace('a', '@').replace('e', '&').upper() for nome in lista_nome]
print(usando_replace)

# Exemplo 5
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)
exempo_tupla = [(x, y) for (y, x) in tupla]
print(exempo_tupla)
print(dict(exempo_tupla))
