nome_completo = 'Pedro Henrique do Nascimento Lisboa'
novo_nome = ''
tamanho_nome = len(nome_completo)
contador = 0

while contador < tamanho_nome:
    novo_nome += nome_completo[contador].upper()
    print(novo_nome)
    contador += 1

print(novo_nome)