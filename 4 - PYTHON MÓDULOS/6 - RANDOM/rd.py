import random
import string

# lista_de_nomes = ['Pedro', 'Henrique', 'Juliana', 'Olívia', 'Marcelo', 'Márcia', 'Ana']
#
# # Gera número entre A e B
# interior = random.randint(10, 20)
# flutuante = random.uniform(10, 20)
#
# # Gera número flutuante entre 0 e 1
# zero_e_um = random.random()
#
# # Gera aleatório usando a função range
# com_range = random.randrange(900, 1000, 10)
#
# # Selecionando um item em uma lista
# sorteio = random.choice(lista_de_nomes)
#
# # Selecionando alguns itens em uma lista
# # Com choices pode repetir
# sorteio_2 = random.choices(lista_de_nomes, k=2)
#
# # Com sample não repete
# sorteio_3 = random.sample(lista_de_nomes, k=2)
#
#
# print(interior)
# print(flutuante)
# print(zero_e_um)
# print(com_range)
# print(sorteio)
# print(sorteio_2)
# print(sorteio_3)
#
# # Embaralhando uma lista
# random.shuffle(lista_de_nomes)
# print(lista_de_nomes)

# Gerador de senha.
letras = list(string.ascii_letters)
numeros = list(string.digits)
caracteres = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '-', '+', '=']
tudo = [*letras, *numeros, *caracteres]

tamanho_senha = int(input('Informe o tamanho da sua senha: '))
nova_senha = "".join(random.choices(tudo, k=tamanho_senha))

print(nova_senha)

