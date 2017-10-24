from socket import *
host = "" #host is leeg zodat hij van uit alle host kan werken
port = 12397

connectie = socket(AF_INET, SOCK_STREAM)
connectie.bind((host, port))
connectie.listen(5)

print("Server wacht op connectie.....")
q,addr = connectie.accept()

while True:
	server_message = input("Voer data in om naar de client te sturen: ")
	if server_message !="":
		server_message = bytearray(server_message, 'utf-8')
		q.send(server_message)
	else:
		client_message = q.recv(1024)
		print("Bericht van de client : {}" .format(client_message))