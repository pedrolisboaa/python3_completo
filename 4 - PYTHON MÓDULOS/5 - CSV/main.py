import csv

with open('clientes.csv', 'r', encoding="utf-8") as arquivo:
    dados = csv.reader(arquivo)

    for dado in dados:
        print(dado)

