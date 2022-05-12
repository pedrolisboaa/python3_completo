usuario = input("Digite seu nome de usuário: ")

if len(usuario) > 15 or len(usuario) <= 6:
    print(f'Usuário {usuario} é invalido.')
else:
    print(f'usuário {usuario} é valido ')