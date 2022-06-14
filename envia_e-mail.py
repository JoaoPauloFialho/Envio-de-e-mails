from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as arquivo:
    template = Template(arquivo.read()) #não esquecer do read quando for ler um arquivo
    data = datetime.now().strftime('%d/%m/%Y')
    msg_html = template.safe_substitute(nome='Nome', data=data) #esse safe_substitute é para não levantar exceção caso falte place holder

msg = MIMEMultipart()
msg['from'] = meu_email #quem vai enviar
msg['to'] = 'Email cliente'
msg['subject'] = 'Assunto E-mail'

corpo_msg = MIMEText(msg_html, 'html') #se fosse texto simples era só escrever mas como é html precisa especificar
msg.attach(corpo_msg) #esse atach se usa para inserir algo na mensagem

with open('imagem.jpg', 'rb') as image:
    img = MIMEImage(image.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso.')
