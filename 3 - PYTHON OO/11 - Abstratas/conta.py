from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def verificar_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo:.2f}')

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo += valor
            self.detalhes()
            return
        raise ValueError('Saldo precisa ser numérico.')

    def detalhes(self):
        print(f'Agência: {self.agencia}, conta {self.conta} Saldo: R${self.saldo}')

    @abstractmethod
    def sacar(self):
        pass

