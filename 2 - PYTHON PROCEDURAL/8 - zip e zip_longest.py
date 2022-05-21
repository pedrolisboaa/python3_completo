"""
zip - unindo iteraveis
zip_longest - Itertools
"""
import itertools

cidades_df = ['Guará', 'Lago Sul', 'Lago Norte', 'Asa Sul', 'Asa Norte']
quadras_df = ['QI', 'QL', 'QLN', 'SQS']

cidades_quadras = zip(cidades_df, quadras_df)
cidades_quadras_longests = itertools.zip_longest(cidades_df, quadras_df, fillvalue='VISHHHH')
for n in cidades_quadras_longests:
    print(n)

for n in cidades_quadras:
    print(f'{n[0]} - {n[1]}')

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
string = 'pedropedro'
todos_numeros = zip(numeros, string)
print(list(todos_numeros))
print(dict(todos_numeros))
for n in todos_numeros:
    print(n)


