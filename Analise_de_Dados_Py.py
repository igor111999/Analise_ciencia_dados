import pandas as pd

tabela = pd.read_csv("/content/drive/MyDrive/Minicurso Analise de Dados/ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
display(tabela)

tabela = tabela.dropna()
display(tabela.info())

display(tabela.describe().round(1))

qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
display(qtde_categoria_perc)


import plotly.express as px

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()
