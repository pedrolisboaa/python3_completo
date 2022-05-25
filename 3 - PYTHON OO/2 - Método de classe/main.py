from pessoa import Pessoa

p1 = Pessoa('Pedro', 29)
p1.ano_nascimento()
print(p1.ANO_ATUAL)
print(p1.gerar_id())

print(Pessoa.gerar_id())
