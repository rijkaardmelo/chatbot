from flask import Flask, make_response, jsonify, render_template, send_from_directory, request, redirect, url_for
from werkzeug.utils import secure_filename
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from time import sleep
import pandas
import os

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder='frontend/build/static', template_folder='frontend/build')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message" : "No file part"}), 500
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message" : "No selected file"}), 500
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "File successfully uploaded"}), 201
    
@app.route("/file", methods=["GET"])
def list_file():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        fileaddress = os.path.join(UPLOAD_FOLDER, filename)
        if(os.path.isfile(fileaddress)):
            files.append({
                'filename': filename,
                'fileaddress': path + "\\" + UPLOAD_FOLDER + "\\" + filename
                })
    return jsonify(files)

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.get_json()['message']
    if(is_connected()):
            try:
                for contato in contatos.values:
                    link = f'https://web.whatsapp.com/send?phone={contato[1]}&text={message}'
                    driver.get(link)
                    while len(driver.find_elements(By.ID, 'side')) < 1:
                        sleep(1)
                    sleep(5)
                    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                    sleep(5)
            except:
                return make_response(jsonify('Erro enviar'), 400)
    else:
        return make_response(jsonify("Erro conectar"), 400)
    return make_response(jsonify('Enviado'), 200)

@app.route("/send_document", methods=["POST"])
def send_document():
    address = request.get_json()['selectedItem']
    try:
        for contato in contatos.values:
            link = f'https://web.whatsapp.com/send?phone={contato[1]}'
            driver.get(link)
            while len(driver.find_elements(By.ID, 'side')) < 1:
                sleep(1)
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/span').click()
            sleep(2)
            keyboard = Controller()
            keyboard.type(address)
            keyboard.press(Key.enter)
            sleep(2)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
            # sleep(5)
    except:
        return make_response(jsonify('Erro enviar'), 400)
    return make_response(jsonify('Enviado'), 200)

@app.route("/send_media", methods=["POST"])
def send_media():
    address = request.get_json()['selectedItem']
    try:
        for contato in contatos.values:
            link = f'https://web.whatsapp.com/send?phone={contato[1]}'
            driver.get(link)
            while len(driver.find_elements(By.ID, 'side')) < 1:
                sleep(1)
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/span').click()
            sleep(2)
            keyboard = Controller()
            keyboard.type(address)
            keyboard.press(Key.enter)
            sleep(2)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
            # sleep(5)
    except:
        return make_response(jsonify('Erro enviar'), 400)
    return make_response(jsonify('Enviado'), 200)

@app.route('/', methods=['GET'])  
def index():
    return render_template('index.html')
    
if __name__ == '__main__':

    contatos = pandas.read_csv("Contatos.csv")

    path = os.getcwd()
    profile = os.path.join(path, "whatsapp")

    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir={}".format(profile))

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

    app.run()