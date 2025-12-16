get_ipython().system(' Pip install Selenium')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

navegador.quit()

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_euro)

navegador.quit()

navegador = webdriver.Chrome()
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)
navegador.quit()

import pandas as pd 

tabela = pd.read_excel('Produtos.xlsx')
display(tabela)

tabela.loc[tabela['Moeda']== 'Dólar','Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda']== 'Euro','Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda']== 'Ouro','Cotação'] = float(cotacao_ouro)

tabela['Preço de Compra']= tabela['Preço Original'] * tabela['Cotação']

tabela['Preço de Venda']= tabela['Preço de Compra'] * tabela['Margem']

display(tabela)

tabela.to_excel('produto novoss.xlsx', index=False)




