string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = string.split('9')
lista.pop()
lista = [n.replace('012345678', '0123456789') for n in lista]
print(lista)

nova_lista = '.'.join(lista)
print(nova_lista)