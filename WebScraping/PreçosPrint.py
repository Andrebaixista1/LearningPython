import pandas as pd
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome(executable_path="chromedriver.exe")


# Convites de Casamento (Brilhoso) - 100 Uni. Frente e Verso - 16x22cm
# def convites
navegador.get('https://www.printi.com.br/configuracao-convite-de-casamento')

time.sleep(10)


# PERSONALIZADO
personalizado1 = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div/div[2]/div/div[2]/label/div').click()
time.sleep(2)
# TAMANHO
size1 = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[2]/div/div[6]/label/img').click()
time.sleep(2)
# DIGITAR TAMANHO 
# digitarTamanho = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[5]/div/div[2]/span[1]/label/input').click()
# time.sleep(1)
larguraConvite = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[5]/div/div[2]/span[1]/label/input').send_keys('16' + Keys.TAB)
alturaConvite = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[5]/div/div[2]/span[2]/label').send_keys('22')
confirma = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[5]/div/div[3]/div[2]/button[2]').click()
time.sleep(4)
# IMPRESSÃO FRENTE E VERSO

frenteEVerso = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[3]/div/div[1]/label/div').click()
time.sleep(2)

# PAPEL COCHE BRILHOSO 300G

brilhoso300g = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[4]/div/div[2]/label/div').click()
time.sleep(2)
# ENOBRECIMENTO

semEnobrecimento = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[6]/div/div[2]/label/div').click()
time.sleep(2)

# EXTRAS

semExtras = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[2]/div[2]/div[7]/div/div[1]/label/div').click()
time.sleep(5)



# Calculo de Frete 

cep_frete = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[2]/span/label/input').send_keys('02350003' + Keys.ENTER)
# cep_frete = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[2]/span/label/button/svg/g/path').click()
time.sleep(10)
quantidade100 = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[4]/table/tbody/tr[2]/td[5]/label/span[1]').click()
# quantidade = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[4]/div/button/svg').click()
# time.sleep(7)
# quantidade = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[4]/table[2]/tbody/tr/td[1]/span/label/input').send_keys('100')

# quantidade = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/main/div[3]/div[2]/div[4]/table[2]/tbody/tr/td[1]/span/label/button/svg').click()



# RESUMO GERAL DOS DADOS

sleep(5)
produto = 'Convites de Casamento (Brilhoso) - 100 Uni. Frente e Verso - 16x22cm'
formato = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[1]')
formato = formato.text


impressao = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[2]')
impressao = impressao.text


cores = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[3]')
cores = cores.text


papel = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[4]')
papel = papel.text


acabamento = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[5]')
acabamento = acabamento.text


enobrecimento = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[6]')
enobrecimento = enobrecimento.text


extras = navegador.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/ul/li[7]')
extras = extras.text


sleep(1)

print('Resumo')
# print(*-**5)
print(produto)
print(formato)
print(impressao)
print(cores)
print(papel)
print(acabamento)
print(enobrecimento)
print(extras)

