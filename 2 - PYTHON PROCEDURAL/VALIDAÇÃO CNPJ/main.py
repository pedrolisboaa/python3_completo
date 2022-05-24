import CNPJ

if __name__ == '__main__':
    while True:
        cnpj = input(f'Informe um CNPJ, somente digitos: ')
        cnpj_cortado = cnpj[:-2]

        primeiro_digito = CNPJ.calcular_digito(cnpj_cortado, CNPJ.PRIMEIRO_VALIDADOR)
        segundo_digito = CNPJ.calcular_digito(cnpj_cortado, CNPJ.SEGUNDO_VALIDADOR, primeiro_digito)
        novo_cnpj = CNPJ.arrumar_cnpj(cnpj, primeiro_digito, segundo_digito)
        print(CNPJ.validando_o_cnpj(cnpj, novo_cnpj))

        continuar = input(f'Deseja continuar [S]im [N]ão: ').upper()
        if continuar != 'S':
            break

print('FIM PROGRAMA.')
