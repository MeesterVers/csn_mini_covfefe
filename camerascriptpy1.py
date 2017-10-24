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
fromaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"
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
def mailac():
    msg = MIMEMultipart()
    fromaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"   #email van verzender
    toaddr = "marczoomers@gmail.com"    #email van ontvanger
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
    server.login(fromaddr, "") #wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("mail is verstuurd naar:"+toaddr)
def mailde():
    msg = MIMEMultipart()
    fromaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"   #email van verzender
    toaddr = "marczoomers@gmail.com"    #email van ontvanger
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarmdeactivatie"
    body = "Het alarm is geactiveerd en de deactivatieprocedure is doorgevoerd."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, "") #wachtwoord van het verzend emailadress
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
	    time.sleep(20)
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
    mailde()
    
