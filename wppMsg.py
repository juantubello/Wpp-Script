from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)
flag = ""
while flag != "n":
    name = input('Ingresa nombre del contacto ')
    msg = input('Ingresa el mensaje a enviar ')
    count = int(input('Ingrese cuantas veces va a enviar el mensaje '))

    input('Inicie sesión con su código QR, una vez dentro presione cualquier tecla ')

    user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
    flag = input('¿Quiere mandar otro mensaje? (s/n) ').lower()
