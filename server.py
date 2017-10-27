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
		print(client_message)
		if(str(client_message) == "b'alarm_on'"):
			print("DO DIT SHIT")
Thread(target=ontvangbericht).start()

def send_to_client(server_message):
		server_message = bytearray(server_message, 'utf-8')
		q.send(server_message)
send_to_client("disarm")