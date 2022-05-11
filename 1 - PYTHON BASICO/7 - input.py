"""
Entrada de dados!!
"""
from datetime import datetime

nome = input('Informe seu nome: ')
idade = int(input('Quantos anos você tem? '))
nascimento = datetime.today().year - idade

print(f'{nome.capitalize()} então você nasceu em {nascimento}')