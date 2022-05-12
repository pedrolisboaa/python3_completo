"""
Problema 1
"""
# numero = input('Informe um número: ')
#
# if numero.isdigit():
#     numero = int(numero)
#     if numero % 2 == 0:
#         print(f'{numero} é par.')
#     else:
#         print(f'{numero} é impar.')
# else:
#     print(f'{numero} não é um inteiro.')

"""
Problema 2
"""

# hora = int(input('Informe a hora: '))
# if 0 < hora <= 11:
#     print(f'Bom dia!')
# elif 11 < hora <= 17:
#     print(f'Boa tarde!')
# elif 17 < hora <= 24:
#     print('Boa noite!')
# else:
#     print(f'Horário invalido.')

"""
Problema 3 
"""
nome = input('Informe seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f'Seu nome é pequeno.')
elif tamanho_nome <= 6:
    print(f'Seu nome é normal.')
else:
    print(f'Seu nome é grande.')
