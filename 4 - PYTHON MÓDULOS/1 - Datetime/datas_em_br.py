from datetime import datetime
from locale import setlocale, LC_ALL


# Mudando o local para atualizar a data
setlocale(LC_ALL, 'pt_BR.utf-8')
dt = datetime.now()
dt_formatada = dt.strftime('%A, %d de %B de %Y')
print(dt)
print(dt_formatada)


