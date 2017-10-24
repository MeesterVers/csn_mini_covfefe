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

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
i=0
print("Het alarm is actief")
moment=strftime("%Y-%m-%d_%H%M")
print(moment)

def contactcentrale():
    #TBU deze functie moet de foto en de info naar de alarmcentrale sturen
activatie='Het alarm is geactiveerd'
deactivatie='Het alarm is gedeactiveerd'

try:
    while True:
        input_state = GPIO.input(12)
	        output_state = GPIO.input(22)
        if(GPIO.input(12)==GPIO.LOW):
            print(activatie)
            subprocess.call("/home/pi/webcam/webcam.sh",shell=True)
            GPIO.output(18,GPIO.HIGH)
            moment=strftime("%Y-%m-%d_%H%M")
            print('Foto gemaakt')
            print('20 seconden deactivatietijd voor het verzenden van mail met foto van alarmactivatie')
	        time.sleep(20)
	        contactcentrale() #TBU hier moet een functie die de foto en de info naar de alarmcentrale stuurt
	        GPIO.output(18,GPIO.LOW)
	        break
	elif(GPIO.input(22)==GPIO.HIGH):
	    GPIO.output(18,GPIO.LOW)
	elif(GPIO.input(22)==GPIO.LOW):
	    GPIO.output(18,GPIO.HIGH)
        i=i+1
except KeyboardInterrupt:
    GPIO.cleanup()
    print(deactivatie)