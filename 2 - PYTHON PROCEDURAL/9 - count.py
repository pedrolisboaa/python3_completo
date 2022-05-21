"""
count - itertools
"""

from itertools import count

contador = count(start=1)
# for n in contador:
#     print(round(n, 2))
#     if n > 10000:
#         break


nomes = ['Pedro', 'Juliana', 'Marcia']
print(list(zip(contador, nomes)))