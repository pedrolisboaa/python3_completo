PRIMEIRO_VALIDADOR = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
SEGUNDO_VALIDADOR = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def calcular_digito(cnpj, lista, digito=None):
    if digito != None:
        cnpj = f'{cnpj}{digito}'

    somador = 0
    for i in range(len(lista)):
        somador += int(cnpj[i]) * lista[i]

    calculo = 11 - (somador % 11)

    if calculo > 9:
        return 0
    return calculo


def arrumar_cnpj(cnpj, digito1, digito2):
    cnpj = cnpj[:-2]
    return f'{cnpj}{digito1}{digito2}'


def validando_o_cnpj(cnpj_antigo, cnpj_novo):
    if cnpj_antigo == cnpj_novo:
        return f'CNPJ Válido'
    return f'CNPJ invalido'
