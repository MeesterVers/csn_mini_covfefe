from socket import *
from threading import Thread, Lock
_db_lock = Lock()

host = "192.168.178.138" #ip van de host (server)
port = 12397
connectie = socket(AF_INET, SOCK_STREAM)

connectie.connect((host, port))
print("Alarm client socket inorde")
print("Er is nu connectie met de server..")

def ontvangbericht():
	while True:
		server_message = connectie.recv(1024)
		print("Bericht van de client : {} \n" .format(server_message))
Thread(target=ontvangbericht).start()

while True:
	client_message = input("Send message: ")
	client_message = bytearray(client_message, 'utf-8')
	connectie.send(client_message)
