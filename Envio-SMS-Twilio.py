import pandas as pd

# Criando uma lista com o nome dos primeiros 6 meses do ano.
months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Loop FOR fazendo a leitura das bases de dados no formato excel mediante a cada mês que está sendo analisado
for month in months:
    print(month)
    sales_table = pd.read_excel(fr'C:\Users\jonat\Documents\Meus Projetos\Python\Projeto 4 Envio SMS Twilio\Envio-SMS-Twilio\Relatório de Vendas\{month}.xlsx')
    print(sales_table)
