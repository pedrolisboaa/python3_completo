from datetime import datetime

nome = 'Pedro'
idade = 29

peso = 130
altura = 1.90

ANO_ATUAL = datetime.today().year
ANO_DE_NASCIMENTO = ANO_ATUAL - idade
IMC = peso / altura ** 2

print(f'{nome} tem {idade} anos ele nasce em {ANO_DE_NASCIMENTO}')
print(f'{nome} pesa {peso}K, mede {altura} e seu IMC = {IMC:.2f}')




