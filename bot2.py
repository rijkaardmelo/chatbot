from flask import Flask, make_response, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from time import sleep
import pandas
import os

app = Flask(__name__)

# def is_connected():
#     time = 0
#     while time < 60:
#         try:
#             if driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[2]/div[2]/div/div/div/div/img'):
#                 return True
#         except:
#             time +=1
#             sleep(1)
#     return False

# @app.route("/send_message", methods=["GET"])
# def send_message():
#     if(is_connected()):
#         for contato in contatos.values:
#             try:
#                 link = f'https://web.whatsapp.com/send?phone={contato[1]}&text=Olá'
#                 driver.get(link)
#                 while len(driver.find_elements(By.ID, 'side')) < 1:
#                     sleep(1)
#                 sleep(5)
#                 driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
#                 sleep(5)
#                 return make_response(jsonify('Enviado'), 200)
#             except:
#                 return make_response(jsonify('Erro enviar'), 400)
#     else:
#         return make_response(jsonify("Erro conectar"), 400)

# def send_document():
#     for contato in contatos.values:
#         try:
#             link = f'https://web.whatsapp.com/send?phone={contato[1]}'
#             driver.get(link)
#             while len(driver.find_elements(By.ID, 'side')) < 1:
#                 sleep(1)
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/span').click()
#             sleep(2)
#             keyboard = Controller()
#             keyboard.type(r"C:\Users\Rijkaard Melo\Documents\chatbot\file.pdf")
#             keyboard.press(Key.enter)
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
#             sleep(5)
#         except:
#             print(f'Não foi possível enviar documento para {contato[0]}')

# def send_image():
#     for contato in contatos.values:
#         try:
#             link = f'https://web.whatsapp.com/send?phone={contato[1]}'
#             driver.get(link)
#             while len(driver.find_elements(By.ID, 'side')) < 1:
#                 sleep(1)
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/span').click()
#             sleep(2)
#             keyboard = Controller()
#             keyboard.type(r"C:\Users\Rijkaard Melo\Documents\chatbot\flamengo.jpg")
#             keyboard.press(Key.enter)
#             sleep(2)
#             driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
#             sleep(5)
#         except:
#             print(f'Não foi possível enviar documento para {contato[0]}')

@app.route('/', methods=['GET'])  
def home():
    return render_template('index.html')
    
if __name__ == '__main__':

    # contatos = pandas.read_csv("Contatos.csv")

    # path = os.getcwd()
    # profile = os.path.join(path, "whatsapp")

    # options = webdriver.ChromeOptions()
    # options.add_argument(r"user-data-dir={}".format(profile))

    # driver = webdriver.Chrome(options=options)
    # driver.get("https://web.whatsapp.com/")
    # driver.maximize_window()

    app.run()