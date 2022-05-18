"""
Slip - Divide uma string
Join - Junta uma lista
Enumerate - Enumera elementos de uma lista - para iteraveis
"""

# string = 'O Brasil é o pais do futebol, o Brasil é penta.'
# lista = string.split(" ")
# lista_virgula = string.split(',')
# print(lista)
# print(lista_virgula)
#
# for valor in lista:
#     print(f'A palavra "{valor}" aparece {lista.count(valor)}x')
# print('='*100)


nome_completo = 'Pedro Henrique do Nascimento Lisboa'
lista_nome_completo = nome_completo.split()
nome_completo_separado_diferente = "*".join(lista_nome_completo)

print(nome_completo_separado_diferente)

# ENUMERATE

for v1, v2 in enumerate(lista_nome_completo):
    print(f'O indice de {v2} é {v1}')

cpf = '03716477858'
for indice, valor in enumerate(cpf):
    print(f'{indice} = {valor}')



