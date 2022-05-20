from random import randint
# Atividade 1

def saudar(saudacao, nome):
    print(f'{saudacao.capitalize()} {nome.capitalize()}! Como você vai?')


saudar('olá', 'Pedro')


# Atividade 2
def somar_tres(a, b, c):
    return a + b + c


soma = somar_tres(5, 6, 9)
print(soma)


# Atividade 3

def aumento_percentual(valor, porcentagem):
    return valor + (valor * (porcentagem / 100))


aumento = aumento_percentual(500, 100)
print(aumento)


# Atividade 4

def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    if x % 2 == 0:
        return 'Fizz'
    if x % 3 == 0:
        return 'Buzz'
    return x


for i in range(100):
    numero_random = randint(1, 1000)
    resultado = fizz_buzz(numero_random)
    print(f'O número {numero_random} deu {resultado}')
