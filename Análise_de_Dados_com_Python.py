import pandas as pd 
tabela = pd.read_csv('telecom_users.csv')
display(tabela)
 
tabela = tabela.drop('Unnamed: 0', axis = 1)
display(tabela)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors = 'coerce')

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

print(tabela["Churn"].value_counts(normalize= True))
get_ipython().system(' pip install plotly')

import plotly.express as py
for  coluna in tabela.columns:
    grafico = py.histogram(tabela, x=coluna, color= 'Churn', text_auto=True )
    #exibir os graficos 
    grafico.show()
