from socket import *
host = "192.168.1.101" #ip van de host (server)
port = 12397
connectie = socket(AF_INET, SOCK_STREAM)


connectie.connect((host, port))
print("Alarm client socket inorde")
print("Er is nu connectie met de server..")

while True:
	message = connectie.recv(1024)
	print("Bericht van de server : {}" .format(message))