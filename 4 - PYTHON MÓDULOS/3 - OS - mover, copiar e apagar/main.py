import os
import shutil

caminho_original = r'C:\Users\Pedro Henrique\Desktop\pasta teste'
caminho_novo = r'C:\Users\Pedro Henrique\Desktop\pasta_teste_nova'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'A pasta caminho novo já existe.')

#   raiz, diretorios, arquivos
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso.')
