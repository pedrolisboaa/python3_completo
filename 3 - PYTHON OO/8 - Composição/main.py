from classes import Endereco, Cliente

c1 = Cliente('Pedro', 28)
c2 = Cliente('Juliana', 25)

c1.insere_endereco('Brasilia', 'DF')
c1.insere_endereco('São Paulo', 'SP')
c1.insere_endereco('Rio de Janeiro', 'RJ')

c1.mostrar_dados()

c2.insere_endereco('Santa Maria', 'DF')
c2.mostrar_dados()