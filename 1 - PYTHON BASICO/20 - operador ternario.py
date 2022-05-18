"""
Operador ternário
"""

usuario_logado = True
cliente_comeu = True

# Com operador
logado = 'Usuário logado.' if usuario_logado else 'Usuário não está logado'
print(logado)

cliente_no_restaurante = 'O cliente está satisfeito' if cliente_comeu else 'O cliente aguarda seu pedido.'
print(cliente_no_restaurante)


# Sem operador
if usuario_logado:
    print(f'Usuário logado.')
else:
    print(f'Usuário não está logado.')