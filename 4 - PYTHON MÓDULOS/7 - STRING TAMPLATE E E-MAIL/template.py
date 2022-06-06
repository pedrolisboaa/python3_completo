from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


meu_email = 'pedronascimentolisboa@yahoo.com'
minha_senha = 'Pliss99@'

with open('template.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Pedro Lisboa', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Pedro Lisboa'
msg['to'] = meu_email
msg['subject'] = 'Atenção - E-mail teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP_SSL(host='smtp.mail.yahoo.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado')