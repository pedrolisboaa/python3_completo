class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.ferramenta = None

    # Getter
    @property
    def nome(self):
        return self.__nome


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print(f'A caneta esta escrevendo.')


class MaquinaDeEscrever:
    def escrever(self):
        print(f'A maquina de escrever está escrevendo.')


