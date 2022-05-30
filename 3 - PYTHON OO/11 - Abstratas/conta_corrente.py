from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo, )
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print(f'Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()
        return
