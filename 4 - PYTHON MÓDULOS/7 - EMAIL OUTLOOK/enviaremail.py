import win32com.client as win32
from string import Template

# Criando integração com outlook
outlook = win32.Dispatch('outlook.application')

# Criar e-mail
email = outlook.CreateItem(0)

# Ajustando o template de e-mail
with open('email.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    corpo_mensagem = template.substitute(nome='Pedrão', data='Hoje!')

# Configurando e-mail
email.To = 'pedronascimentolisboa@yahoo.com; phlisboa2000@gmail.com'  # Destino
email.Subject = 'E-mail teste'  # Assunto
email.HTMLBody = corpo_mensagem

#anexando arquivos
anexo = r'C:\Users\Pedro Henrique\Desktop\Python 3 completo\4 - PYTHON MÓDULOS\7 - EMAIL OUTLOOK\anexo_teste.txt'
email.Attachments.Add(anexo)

# Essa é uma maneira
# """
# <p>Olá Pedro, vamos vê se isso vai da certo.</p>
# <p>Espero que sim!!</p>
# <br>
# <p>Beijos Pedro!</p>
# """

email.Send()
print('E-mail enviado.')
