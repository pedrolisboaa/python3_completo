from classes import Produto, CarrinhoDeCompras

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('notebook', 5000)
p3 = Produto('caneta', 10)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)

carrinho.listar_produto()
print(carrinho.somar_total())