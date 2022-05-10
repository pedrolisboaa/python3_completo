"""
Variáveis
"""
from datetime import date

ANO_NASCIMENTO = 1992
ANO_ATUAL = date.today().year
IDADE = ANO_ATUAL - ANO_NASCIMENTO

e_maior = IDADE >= 18
peso = 130
altura = 1.90

isso_e_uma_variavel = 'Pedro'
_isso_tambem = 'HENriQue'
mais_uma_1 = 'DO'
mais_outra_2 = 'nascimento'

nome_completo = f'{isso_e_uma_variavel.capitalize()} {_isso_tambem.capitalize()} {mais_uma_1.lower()}'


print(f'{nome_completo} nasceu em {ANO_NASCIMENTO} e seu IMC = {peso / altura ** 2}')
print(f'Possui {IDADE} anos ele é maior de idade? {e_maior}')
