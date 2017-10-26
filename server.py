from socket import *
from threading import Thread, Lock
_db_lock = Lock()
host = "" #host is leeg zodat hij van uit alle host kan werken
port = 12397

connectie = socket(AF_INET, SOCK_STREAM)
connectie.bind((host, port))
connectie.listen(5)

print("Server wacht op connectie.....")
q,addr = connectie.accept()

def ontvangbericht():
	while True:
		client_message = q.recv(1024)
		print("Bericht van de client : {} \n" .format(client_message))
Thread(target=ontvangbericht).start()

while True:
	server_message = input("Send message: ")
	server_message = bytearray(server_message, 'utf-8')
	q.send(server_message)