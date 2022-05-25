"""
public, protected, private
_ privado mais fraco
__ privado mais forte
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


if __name__ == '__main__':
    base = BaseDeDados()

    base.inserir_cliente(1, 'Pedro')
    base.inserir_cliente(2, 'Pedro Henrique')
    base.inserir_cliente(3, 'Pedro Henrique do Nascimento')
    base.inserir_cliente(4, 'Pedro Henrique do Nascimento Lisboa')

    base.listar_clientes()

