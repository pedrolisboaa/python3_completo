from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()
        return

