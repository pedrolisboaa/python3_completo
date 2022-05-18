"""
Desempacotando lista
"""
lista = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'França (Guiana Francesa)',
         'Paraguai', ' Peru', 'Suriname', 'Uruguai', 'Venezuela']

n1, n2, *n3, n4, n5 = lista
m1, m2, m3, *m4 = n3

print(n1)
print(n2)
print(n4)
print(n5)
print(f'*'*10)
print(n3)
print(m1)
print(m2)
print(m3)
print(m4)