import csv

# # Verificando com dicionário
# with open('clientes.csv', 'r', encoding="utf-8") as arquivo:
#     dados = csv.DictReader(arquivo)
#
#     for dado in dados:
#         print(dado)
#
# print(f'------------------------------------------------------------------------------')
#
# # verificando como csv
# with open('clientes.csv', 'r', encoding='utf-8') as a:
#     dados = csv.reader(a)
#
#     for dado in dados:
#         print(dado)

# Lendo o arquivo e salvado na variavel, pois é fechado o arquivo
with open('clientes.csv', 'r', encoding='utf-8') as a:
    dados = [x for x in csv.DictReader(a)]

# Escrevendo um novo arquivo
with open('clientes2.csv', 'w+', encoding='utf-8') as arquivo:
    escreve = csv.writer(arquivo)

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )




