from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self.ligado:
            info = f'{self.nome} não está ligado.'
            print(info)
            self.log_info(info)
            return

        if self.conectado:
            error = f'{self.nome} Já está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self.nome} Está conectado.'
        print(info)
        self.log_info(f'{self.nome} Está conectado.')
        self.conectado = True

    def desconectar(self):
        if not self.conectado:
            error = f'{self.nome} Não está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self.nome} Está desconectado'
        print(info)
        self.log_info(info)
        self.conectado = False

