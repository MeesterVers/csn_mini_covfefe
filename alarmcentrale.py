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

def mailac():
    msg = MIMEMultipart()
    fromaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"   #email van verzender
    toaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"    #email van ontvanger
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarmactivatie"
    body = "Het alarm is geactiveerd en de deactivatieprocedure is niet doorgevoerd. Bijgaand een foto van het moment van activatie van het alarm."
    msg.attach(MIMEText(body, 'plain'))
    moment=strftime("%Y-%m-%d_%H%M")
    filename = moment+".jpg"
    attachment = open("/home/pi/webcam/"+moment+".jpg", "rb") #locatie van foto, To be Updated/editted (henceforth: #TBU)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo #TBU
    server.login(fromaddr, "") #wachtwoord van het verzend emailadress #TBU
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("mail is verstuurd naar:"+toaddr)

def mailde():
    msg = MIMEMultipart()
    fromaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"   #email van verzender
    toaddr = "covfefe.alarmsystem.hu.2k17@gmail.com"    #email van ontvanger
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarmdeactivatie"
    body = "Het alarm is geactiveerd en de deactivatieprocedure is doorgevoerd."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo #TBU
    server.login(fromaddr, "") #wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Mail is verstuurd naar:"+toaddr)