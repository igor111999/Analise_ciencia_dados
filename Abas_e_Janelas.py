
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

import os

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)

navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/figure/a/img').click()

navegador.find_element(By.ID, 'fullname').send_keys("LiraLira")

aba_original = navegador.window_handles[0]
nova_aba = navegador.window_handles[1]
navegador.switch_to.window(nova_aba)
navegador.find_element(By.ID, 'fullname').send_keys("LiraNovaAba")


navegador.find_element(By.ID, 'email').send_keys("lira@lira.com")
for aba in navegador.window_handles:
    navegador.switch_to.window(aba)
    print(navegador.title)

abas = navegador.window_handles
print(len(abas))
nova_janela = navegador.window_handles[2]
navegador.switch_to.window(nova_janela)

navegador.find_element(By.ID, 'fullname').send_keys("LiraJanela")
navegador.find_element(By.ID, 'email').send_keys("janela@lira.com")
navegador.close()
navegador.quit()

