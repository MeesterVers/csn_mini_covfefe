import subprocess
import datetime
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import gmtime, strftime
import pygame
global fromaddr
fromaddr = "alarmsystem.cofveve.hu.2k17@gmail.com"
global toaddr
toaddr = "marczoomers@gmail.com"
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
i=0
print("Het alarm is actief")
moment=strftime("%Y-%m-%d_%H%M")
print(moment)
def alarmsound():
    pygame.mixer.init()
    pygame.mixer.music.load("Audio.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)
    while pygame.mixer.music.get_busy() == True:
        continue
def mailac():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarmactivatie"
    body = "Het alarm is geactiveerd en de deactivatieprocedure is niet doorgevoerd. Bijgaand een foto van het moment van activatie van het alarm."
    msg.attach(MIMEText(body, 'plain'))
    moment=strftime("%Y-%m-%d_%H%M")
    filename = moment+".jpg"
    attachment = open("/home/pi/webcam/"+moment+".jpg", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, "Meme.420") #wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("mail is verstuurd naar:"+toaddr)
def mailde():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarmdeactivatie"
    body = "Het alarm is geactiveerd en de deactivatieprocedure is doorgevoerd."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, "Meme.420") #wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Mail is verstuurd naar:"+toaddr)
try:
    while True:
        input_state = GPIO.input(12)
        output_state = GPIO.input(22)
        if(GPIO.input(12)==GPIO.LOW):
            print("Alarm geactiveerd")
            
            subprocess.call("/home/pi/webcam/webcam.sh",shell=True)
            GPIO.output(18,GPIO.HIGH)
            moment=strftime("%Y-%m-%d_%H%M")
            print('Foto gemaakt')
            print('20 seconden deactivatietijd voor het verzenden van mail met foto van alarmactivatie')
            alarmsound()
            mailac()
            GPIO.output(18,GPIO.LOW)
            break
        elif(GPIO.input(22)==GPIO.HIGH):
            GPIO.output(18,GPIO.LOW)
        elif(GPIO.input(22)==GPIO.LOW):
            GPIO.output(18,GPIO.HIGH)
            i=i+1
except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nAlarm gedeactiveerd")
        pygame.mixer.music.stop()
        mailde()