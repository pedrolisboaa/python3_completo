carrinho = []
produto_1 = carrinho.append(('Produto 1', 30))
produto_2 = carrinho.append(('Produto 2', 40))
produto_3 = carrinho.append(('Produto 3', 50))
produto_4 = carrinho.append(('Produto 4', 60))

# Uma forma
total_produtos = 0
for item in carrinho:
    total_produtos += item[1]
print(f'O total do seu carrinho com {len(carrinho)} produtos deu R$ {total_produtos}')
print('*'*40)

# A forma boa!
forma_boa = sum([total[1] for total in carrinho])
print(forma_boa)

print('*'*40)
# Outra forma tosca
total_produtos2 = [preco[1] for preco in carrinho]
print(total_produtos2)
preco_final_carrinho = lambda *args: sum(args)
print(preco_final_carrinho(*total_produtos2))
