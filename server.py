from socket import *
host = "" #host is leeg zodat hij van uit alle host kan werken
port = 12397

s = socket(AF_INET, SOCK_STREAM)
print("Socket Made")
s.bind((host, port))
print("Socket Bound")
s.listen(5)

print("Listening for connections...")
q,addr = s.accept()
data = input("Enter data to be sent: ")
q.send(data)