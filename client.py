from socket import *
host = "192.168.1.101" #ip van de host (server)
port = 12397
connectie = socket(AF_INET, SOCK_STREAM)

connectie.connect((host, port))
print("Alarm client socket inorde")
print("Er is nu connectie met de server..")

while True:
	client_message = input("Voer data in om naar de client te sturen: ")
	if client_message != "":
		client_message = bytearray(client_message, 'utf-8')
		connectie.send(client_message)
	else:
		server_message = connectie.recv(1024)
		print("Bericht van de server : {}" .format(server_message))