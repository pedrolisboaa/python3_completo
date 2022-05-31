"""
JSON - Javascript Object Notation
é um formato de trocar de dados entre sistemas e programas muito leve e de fácil utilização.
Muito utilizado em APIs
"""

from dados_json import dados
import json

# Exemplo 1 convertendo
listas = list(range(10))
lista_em_json = json.dumps(listas)
print(lista_em_json)
print(type(lista_em_json))

# Exemplo 2 convertendo json para string
dicionario_json_convertido = json.dumps(dados.clientes_dicionario, indent=4)
print(dicionario_json_convertido)
print(type(dicionario_json_convertido))

# Convertendo uma string para dicionario
string_para_json = json.loads(dados.clientes_json)
print(string_para_json)
print(type(string_para_json))

# Pegando um dicionário salvando em um arquivo JSON
with open("clientes2.json", 'w') as arquivo:
    json.dump(dados.clientes_dicionario, arquivo, indent=4)

# Lendo arquivo JSON
with open('clientes2.json', 'r') as arquivo:
    dado = json.load(arquivo)

for chave, valor in dado.items():
    print(chave)
    print(valor)