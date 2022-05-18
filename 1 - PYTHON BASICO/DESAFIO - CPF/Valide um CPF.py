"""
Criando um validador de CPF
"""

CPF_INFORMADO = '15327566152'
NOVO_CPF = CPF_INFORMADO[0:9]

# Validando o primeiro dígito verificador
resultado_soma_da_multiplicacao_do_primeiro_digito = 0

for indice, digito_cpf in enumerate(CPF_INFORMADO[::-1]):
    if indice == 0 or indice == 1:
        continue
    else:
        resultado = indice * int(digito_cpf)
        resultado_soma_da_multiplicacao_do_primeiro_digito += resultado

primeiro_digito_verificador = 11 - (resultado_soma_da_multiplicacao_do_primeiro_digito % 11)

if primeiro_digito_verificador > 9:
    primeiro_digito_verificador = 0

# Validando o segundo digito
resultado_soma_da_multiplicacao_do_segundo_digito = 0

for indice, digito_cpf in enumerate(CPF_INFORMADO[::-1]):
    if indice == 0:
        continue
    else:
        resultado = (indice + 1) * int(digito_cpf)
        resultado_soma_da_multiplicacao_do_segundo_digito += resultado

segundo_digito_verificador = 11 - (resultado_soma_da_multiplicacao_do_segundo_digito % 11)

if segundo_digito_verificador > 9:
    segundo_digito_verificador = 0

# Ajustando o NOVO CPF com os digitos verificadores
NOVO_CPF = f'{NOVO_CPF}{primeiro_digito_verificador}{segundo_digito_verificador}'

# Informando a valida do CPF
mensagem = f'O CPF {CPF_INFORMADO} é valido.' if NOVO_CPF == CPF_INFORMADO else f'O CPF {CPF_INFORMADO} é invalido'
print(mensagem)
