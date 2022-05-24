def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Tu é burro cara? Não existe divisão por zero!')
    return n1 / n2


try:
    print(divide(1, 0))
except ZeroDivisionError as e:
    print(e)
