"""
WHILE
"""
# from time import sleep
#
# contador = 0
# while True:
#     print(contador)
#     if contador == 15:
#         break
#     contador += 1
# print('Acabou o primeiro!')
# sleep(2)
#
# x = 0
# while x < 10:
#     print(x)
#     x += 1
#
# print("Acabou o segundo!")
# sleep(2)

# y = 0
# while y < 100:
#     y += 1
#     if y % 2 == 0:
#         continue
#     else:
#         print(y)

# coluna = 0
# while coluna < 10:
#     linha = 0
#     while linha < 10:
#         print(f'LINHA {linha} - COLUNA {coluna}')
#         linha += 1
#
#     coluna += 1

flag = True
operadores = ['*', '/', '+', '-']

while flag:
    numero_1 = input('Informe um número inteiro: ')
    numero_2 = input('Informe um número inteiro: ')
    operador = input('Informe um operador: ')

    vericacao = numero_1.isnumeric() and numero_2.isnumeric() and operador in operadores

    if not vericacao:
        print(f'Você digitou alguma coisa errada: ')
        print(f'Fim da mini calculadora!')
        break
    else:

        numero_1 = int(numero_1)
        numero_2 = int(numero_2)

        if operador == '+':
            print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
        elif operador == '-':
            print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
        elif operador == '*':
            print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')
        else:
            print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')

    continuar = input('Deseja continuar [S]IM ou [N]AO: ').lower()
    if continuar == 'n':
        break


