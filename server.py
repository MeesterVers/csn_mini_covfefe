from socket import *
host = "" #host is leeg zodat hij van uit alle host kan werken
port = 12397

connectie = socket(AF_INET, SOCK_STREAM)
print("Alarm server socket in orde")
connectie.bind((host, port))
print("Socket Bound")
connectie.listen(5)

print("Server wacht op connectie.....")
q,addr = connectie.accept()

while True:
	message = input("Voer data in om naar de client te sturen: ")
	message = bytearray(message, 'utf-8')
	q.send(message)
