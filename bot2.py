from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas
import os

def is_connected():
    time = 0
    while time < 60:
        try:
            if driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[2]/div[2]/div/div/div/div/img'):
                return True
        except:
            time +=1
            sleep(1)
    return False

def send_message(message):
    for contato in contatos.values:
        try:
            link = f'https://web.whatsapp.com/send?phone={contato[1]}&text={message}'
            driver.get(link)
            while len(driver.find_elements(By.ID, 'side')) < 1:
                sleep(1)

            sleep(5)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            sleep(5)
        except:
            print(f'Não foi possível enviar mensagem para {contato[0]}')
    
if __name__ == '__main__':

    contatos = pandas.read_csv("Contatos.csv")

    path = os.getcwd()
    profile = os.path.join(path, "whatsapp")

    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir={}".format(profile))

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    is_connected()
    send_message("Boa Noite")
    driver.quit()