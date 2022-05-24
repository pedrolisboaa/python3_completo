try:
    a = {}
    print(a)
except NameError as e:
    print('Erro encontrato :', e)
except IndexError as e:
    print(f'O indice não pertence a lista - ', e)
except Exception as e:
    print(f'Erro não identificado - ', e)
finally:
    print(f'Fim do programa!')