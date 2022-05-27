from classes import Escritor, Caneta, MaquinaDeEscrever

escritor1 = Escritor('Pedro')
escritor2 = Escritor('Juliana')

bic = Caneta('bic')
maquina = MaquinaDeEscrever()

escritor1.ferramenta = bic
escritor2.ferramenta = maquina

escritor1.ferramenta.escrever()
escritor2.ferramenta.escrever()


