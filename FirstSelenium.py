import pandas 
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

df = pandas.read_excel('ejemplo1.xls')

url = 'https://api.whatsapp.com/send?phone=0573219490687'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)  # abrir WappWeb
print("Aplicacion titulo wa ",driver.title)
boton1 = '#action-button'
driver.find_element_by_css_selector(boton1).click() # continuar al chat
print("se oprimio CONTINUAR AL CHAT...\n\n")
boton2 = '#header-inner > nav > ul > li:nth-child(1) > a'
driver.find_element_by_css_selector(boton2).click() # usar WappWeb
time.sleep(10) # tiempo para ingresar código QR
#**************

complemento = 'https://api.whatsapp.com/send?phone=0573187173263&text=Hola%20que%20tal?%20espero%20se%20encuentre%20bien,%20cordial%20saludo.'

complemento1 = 'https://api.whatsapp.com/send?phone=057'
complemento2 = '&text='
for i in range(5):
    tel = df['numero'][i]
    mensaje = df['Texto'][i]
    complemento = complemento1+str(tel)+complemento2+mensaje
    driver.get(complemento)  # abrir WappWeb
    time.sleep(4) # tiempo para verificar ingreso
    boton1 = '#action-button'
    driver.find_element_by_css_selector(boton1).click() # continuar al chat
    time.sleep(4) # tiempo para verificar ingreso

    boton2 = '#fallback_block > div > div > a'
    driver.find_element_by_css_selector(boton2).click() # usar WappWeb
    time.sleep(4) # tiempo para verificar ingreso

    boton3 = '#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button > span'
    driver.find_element_by_css_selector(boton3).click() # enviar mensaje
    time.sleep(4) # tiempo para verificar ingreso



print("chat...")
#driver.find_element_by_css_selector(boton2).send_keys('Hola')

print("Aplicacion url es ",driver.current_url)
driver.quit()



