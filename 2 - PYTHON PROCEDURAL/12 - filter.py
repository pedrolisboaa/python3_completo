from dados import pessoas, produtos, lista


maiores_que_cinco = filter(lambda x: x > 5, lista)
pares = filter(lambda x: x % 2 == 0, lista)
print(list(maiores_que_cinco))
print(list(pares))


precos_produtos = filter(lambda x: x['preco'] < 10, produtos)
for _ in precos_produtos:
    print(_)

pessoas_idosas = filter(lambda x: x['idade'] >= 60, pessoas)
for _ in pessoas_idosas:
    print(_)
