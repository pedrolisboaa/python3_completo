# uma função normal
def multiplicacao(arg1, arg2):
    return arg1 * arg2


var = multiplicacao(10, 80)
print(var)

# utilizando lambda
a = lambda x, y: x * y
print(a(10, 80))

# outra lambda
nome_maisculo = lambda a: a.upper()
print(nome_maisculo('Pedro'))

