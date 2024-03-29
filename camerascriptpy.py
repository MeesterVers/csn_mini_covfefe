#Imported libraries

import subprocess
import datetime
import RPi.GPIO as GPIO
import sys
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import gmtime, strftime
import pygame
from socket import *
from threading import Thread, Lock  # import end

#declarations

global fromaddr  # email verwijzing start
fromaddr = "alarmsystem.cofveve.hu.2k17@gmail.com"
global toaddr
toaddr = "marczoomers@gmail.com"  # email verwijzing end

_db_lock = Lock()  # client variabelen start
global host
host = "192.168.42.2"  # ip van de host (server)
global port
port = 12397 # port van verbinding
connectie = socket(AF_INET, SOCK_STREAM)  # client variabelen end



engels1 = 'choose a language'  # talen start menu variabelen
duits1 = 'wähle eine Sprache'
japans1 = '言語を選択する(Gengo o sentaku suru)'
spaans1 = 'elige un idioma'
frans1 = 'choisissez une langue'
engels2 = '1:english'
duits2 = '2:Deutsche'
japans2 = '3:日本語(Nihongo)'
spaans2 = '4:Español'
frans2 = '5:français'  # talen start  enu end


def language():  # invoer van taalkeuze functie
    kloppend = False
    userinput = input('1-5: ')
    while kloppend == False:
        global choice
        if userinput in ('1', '2', '3', '4', '5'):
            kloppend = True
            choice = userinput
        else:
            print('error')
            userinput = input('1-5: ')


def taalopties(choice):  # verwerking van talen
    global alarmtekst, mailsubac, mailbodyac, mailsendtext, mailsubde, mailbodyde, fotomade, timebefore, alarmdec
    if choice == '1':  # engels
        print('Hello cruel world')
        alarmtekst = 'Alarm activated'  # alarm
        mailsubac = 'Alarmactivation'  # def mailac
        mailbodyac = 'The alarm has been activated and the deactivation procedure has not been completed. Attached a picture of the moment of activation of the alarm.'  # def mailac
        mailsendtext = ''  # def mailac & def mailde
        mailsubde = 'mail has been sent to: '  # mailde
        mailbodyde = 'The alarm has been deactivated and the deactivation procedure has been executed.'  # mailde
        fotomade = 'Photo made'  # alarm
        timebefore = '20 seconds deactivation time for sending mail with photo of alarm activation'  # alarm
        alarmdec = 'Alarm deactivated'  # alarm
    elif choice == '2':  # duits
        print('Hallo grausame Welt')

        alarmtekst = 'Alarm aktiviert'  # alarm
        mailsubac = 'Alarmaktivierung'  # def mailac
        mailbodyac = 'Der Alarm wurde aktiviert und die Deaktivierungsprozedur wurde nicht abgeschlossen. Hat ein Bild des Momentes der Aktivierung des Alarms angebracht.'  # def mailac
        mailsendtext = 'Mail wurde gesendet an: '  # def mailac & def mailde
        mailsubde = 'Alarmdeaktivierung'  # mailde
        mailbodyde = 'Der Alarm wurde deaktiviert und die Deaktivierungsprozedur wurde ausgeführt.'  # mailde
        fotomade = 'Foto gemacht'  # alarm
        timebefore = '20 Sekunden Deaktivierungszeit zum Senden von Mail mit Foto der Alarmaktivierung'  # alarm
        alarmdec = 'Alarm deaktiviert'  # alarm
    elif choice == '3':  # anime
        print("こんにちは残酷な世界 (Kon'nichiwa zankokuna sekai)")

        alarmtekst = 'アラーム起動'  # alarm
        mailsubac = 'アラームアクティベーション'  # def mailac
        mailbodyac = 'アラームがアクティブにされ、非アクティブ化手順が完了していません。 アラームの起動の瞬間の写真を添付しました。'  # def mailac
        mailsendtext = 'メールが送信されました： '  # def mailac & def mailde
        mailsubde = 'アラーム解除'  # mailde
        mailbodyde = 'アラームが解除され、非アクティブ化手順が実行されました。'  # mailde
        fotomade = '写真製作'  # alarm
        timebefore = 'アラーム起動の写真付きメール送信のための20秒の非アクティブ化時間'  # alarm
        alarmdec = 'アラームが無効になった'  # alarm
    elif choice == '4':  # spaans
        print('Hola mundo cruel')

        alarmtekst = 'Alarma activada'  # alarm
        mailsubac = 'Alarmactivación'  # def mailac
        mailbodyac = 'La alarma se activó y el procedimiento de desactivación no se completó. Adjunta una foto del momento de activación de la alarma.'  # def mailac
        mailsendtext = 'El correo ha sido enviado a: '  # def mailac & def mailde
        mailsubde = 'Desactivación de alarma'  # mailde
        mailbodyde = 'La alarma se ha desactivado y se ha ejecutado el procedimiento de desactivación.'  # mailde
        fotomade = 'Foto hecha'  # alarm
        timebefore = '20 segundos de tiempo de desactivación para enviar correos con foto de activación de alarma'  # alarm
        alarmdec = 'Alarma desactivada'  # alarm
    elif choice == '5':  # frans
        print('Bonjour monde cruel')

        alarmtekst = "Alarme activée"  # alarm
        mailsubac = "Alarmactivation"  # def mailac
        mailbodyac = "L'alarme a été activée et la procédure de désactivation n'a pas été terminée. Attaché une image du moment de l'activation de l'alarme."  # def mailac
        mailsendtext = "Le courrier a été envoyé à:"  # def mailac & def mailde
        mailsubde = "Alarmdeactivation"  # mailde
        mailbodyde = "L'alarme a été désactivée et la procédure de désactivation a été exécutée."  # mailde
        fotomade = "Photo faite"  # alarm
        timebefore = "Temps de désactivation de 20 secondes pour l'envoi de courrier avec photo de l'activation de l'alarme"  # alarm
        alarmdec = "Alarme désactivée"  # alarm


def ontvangbericht(): #uitvoer wanneer er een bericht ontvangen wordt van de server
    while True:
        server_message = connectie.recv(1024)
        print("Bericht van de client : {} \n".format(server_message))
        GPIO.cleanup()
        print("\n" + alarmdec)
        pygame.mixer.music.stop()
        mailde()
        print('cuck')
        global andereparameter
        andereparameter = False
        global randomparameter
        randomparameter = False
        disconnect()
        os._exit(0)


def disconnect(): #disconnect van de server
    connectie.close
    print('Disarmed')


def alarmsound():  # alarm sound function
    pygame.mixer.music.load(audio + ".mp3")
    pygame.mixer.music.play(9000)
    pygame.mixer.music.set_volume(1)
    while pygame.mixer.music.get_busy() == True:
        continue


def playbeep():  # beep sound function
    pygame.mixer.music.load("Beep.mp3")
    pygame.mixer.music.play(9)
    pygame.mixer.music.set_volume(1)
    while pygame.mixer.music.get_busy() == True:
        continue


def mailac():  # activation mail function
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = mailsubac
    body = mailbodyac
    msg.attach(MIMEText(body, 'plain'))
    filename = moment + ".jpg"
    print(filename)
    attachment = open("/home/pi/webcam/" + filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, "Meme.420")  # wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(mailsendtext + toaddr)


def mailde():  # deactivation mail function
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = mailsubde
    body = mailbodyde
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, "Meme.420")  # wachtwoord van het verzend emailadress
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(mailsendtext + toaddr)


#hoofdprogramma

connectie.connect((host, port))  # setting up connection w/ server
print("conn_w/_:192.168.42.2 ok")
print("Er is nu connectie met de server..")

Thread(target=ontvangbericht).start() #client stelt zich open om constant berichten te ontvangen van de server

print('{} / {} / {} / {} / {}'.format(engels1, duits1, japans1, spaans1, frans1)) #Vraagt in iedere taal om een taalkeuze te maken
print('{}\n{}\n{}\n{}\n{}'.format(engels2, duits2, japans2, spaans2, frans2)) #Noemt de taalkeuzes met bijbehorende keuze-waarde op
language()  #vraagt naar gewenste taal
taalopties(choice) #geeft de keuzeopties voor talen weer met corresponderende invoerwaarde

global audio  # audio langauge selection start
audio = choice #correcte taal alarm wordt vastgesteld
audio = str(audio)
pygame.mixer.init()  # audio langauge selection end

GPIO.setmode(GPIO.BOARD)  # GPIO setup start
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup van de buttons (vervanging van de bewegingssensor)
GPIO.setup(18, GPIO.OUT)                          #setup van het lampje
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup van de aarding


login = True #login sequence
while login == True:
    wachtwoordovereenkomend = False
    while wachtwoordovereenkomend == False: #vraagt naar wachtwoord
        wachtwoord = input("Password: ")
        if wachtwoord in ('bingo673', 'wachtwoord', 'geheim'): #vergelijkt wachtwoord met correcte opties
            wachtwoordovereenkomend = True                      #breekt uit de login
        else:                                       #foutief wachtwoord invoer vraagt opnieuw naar wachtwoord
            print('error')
            wachtwoord = input('Password: ')


alarminactief = True #alarmactivatie process
while alarminactief == True:
    if (GPIO.input(12) == GPIO.LOW): #button ingedrukt
        print(alarmtekst)           #waarschuwt dat het alarm actief is
        global moment
        moment = strftime("%Y-%m-%d_%H%M") #tijdsopname
        client_message = ("Cofveve activated")  #stuurt naar de server dat alarm geactiveerd is
        if client_message != '': #vertaald het bericht naar bytes om naar de server te sturen
            client_message = bytearray(client_message, 'utf-8')
            connectie.send(client_message)
        subprocess.call("/home/pi/webcam/webcam.sh", shell=True) #foto maken sequence
        GPIO.output(18, GPIO.HIGH) #lampje gaat aan
        print(fotomade)
        print(timebefore)
        playbeep() #waarschuwt dat het alarm afgegaan is
        mailac()    #stuurt mail dat alarm geactiveerd is
        alarmsound() #speelt het alarm voor 5 uur af wanneer het alarm niet binnen 20 seconden afgezet is
        GPIO.output(18, GPIO.LOW) #zet het lampje uit
