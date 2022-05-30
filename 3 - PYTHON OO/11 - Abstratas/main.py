from poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.sacar(500)

print('-----------------------------')

cc = ContaCorrente(3333, 1212, 0)
cc.depositar(100)
cc.depositar(100)
cc.sacar(250)
