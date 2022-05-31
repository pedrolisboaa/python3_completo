"""
https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime, timedelta

data = datetime(1992, 9, 15)
print(f'Data no formato americano - {data}')
print(f'Data no formato brasileiro - {data.strftime("%d/%m/%Y")}')
print(f'Data no formato brasileiro diferente - {data.strftime("%d/%B/%Y")}')

# Recebendo datas
data2 = datetime.strptime('23/08/2021', '%d/%m/%Y')
print(data2)

# Pegando o timestamp
time_stamp_olivia = datetime.timestamp(data2)
print(time_stamp_olivia)
print(f'-----------------------------')

nascimento_juliana = datetime.strptime('22/8/1996', '%d/%m/%Y')
nova_data = nascimento_juliana + timedelta(seconds=10)
print(nova_data)

dif = data - nascimento_juliana
print(dif)