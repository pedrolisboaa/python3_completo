"""
IF, ELIF, ELSE
"""
from getpass import getpass

usuarios_banco = ['pepelisboa', 'jujudanada', '123deoliviera4']
senhas_global = 123456

usuario = input('Informe seu usuário: ')
#senha = input('Informe sua senha: ')
senha = getpass('Informe sua senha: ')

if usuario in usuarios_banco and senha == senhas_global:
    print(f'Usuário logado')
else:
    print(f'Você não pode logar')
