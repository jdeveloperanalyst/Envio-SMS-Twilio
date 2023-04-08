import pandas as pd
from twilio.rest import Client
from Credenciais import secret
from time import sleep

# Criando variáveis no qual se refere ao SID(usuário) e um token(autenticação) criado no site twilio.com/console para que seja possível uma conexão ao twilio para envio da menssagem
account_sid = secret['sid']
auth_token = secret['token']
client = Client(account_sid, auth_token)

# Criando uma lista com o nome dos primeiros 6 meses do ano.
months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Loop FOR fazendo a leitura das bases de dados no formato excel mediante a cada mês que está sendo analisado
for month in months:
    sales_table = pd.read_excel(fr'C:\Users\jonat\Documents\Meus Projetos\Python\Projeto 4 Envio SMS Twilio\Envio-SMS-Twilio\Relatório de Vendas\{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any():
        seller = sales_table.loc[(sales_table['Vendas'] > 55000), 'Vendedor'].values[0]
        sale = sales_table.loc[(sales_table['Vendas'] > 55000), 'Vendas'].values[0]
        print(f'No mês de {month}, o vendedor {seller} bateu a meta com {sale} vendas!')
        sleep(3)
        # Envio do SMS
        sms = client.messages.create(
            to=secret['my_cellphone'],
            from_=secret['twilio_phone'],
            body=f'No mês de {month}, o vendedor {seller} bateu a meta com {sale} vendas!')
        sleep(3)
        print(sms.sid)
