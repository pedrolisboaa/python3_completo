"""
No python, o comportamento dos operadores é definido por métodos especiais
Vamos alterar o comportamento de operadores com classes definidas pelo usuário
"""


class Retangulo():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x + novo_y)


rec1 = Retangulo(5, 10)
rec2 = Retangulo(15, 10)
rec3 = rec1 + rec2
print(rec3.y)
print(rec3.x)
