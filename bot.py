import pandas
import pyautogui
import pyscreeze
import webbrowser
from time import sleep

contatos = pandas.read_csv("Contatos.csv")
for contato in contatos.values:
    mensagem = f'Olá {contato[0]}'
    try:
        link = f'https://web.whatsapp.com/send?phone={contato[1]}&text={mensagem}'
        webbrowser.open(link)
        sleep(10)
        enviar = pyscreeze.locateCenterOnScreen("Enviar.png")
        sleep(2)
        pyautogui.click(enviar)
        sleep(2)
        pyautogui.hotkey('ctrl','w')
        sleep(2)
    except:
        print(f'Não foi possível enviar mensagem para {contato[0]}')