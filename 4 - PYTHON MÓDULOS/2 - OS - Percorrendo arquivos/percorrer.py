import os

caminho_procura = r'C:\Users\Pedro Henrique\Downloads'
termo_procura = 'Teorico'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Tamanho: ', tamanho_arquivo)
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido, ', e)