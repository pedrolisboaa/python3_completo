var_1 = 'pedro'
var_2 = 'lisboa'

print(var_1 != var_2 and var_2 == var_2)

idade_votar_nao_obrigatorio = 16
idade_votar_obrigatorio = 18

idade = int(input('Informe sua idade: '))

if idade < idade_votar_nao_obrigatorio:
    print(f'Você não pode votar.')
elif idade_votar_nao_obrigatorio <= idade >= idade_votar_obrigatorio:
    print(f'Você é obrigado a votar')