import socket
from time import *

def connexionserveur():
    global client
    adresseIP = "176.130.194.32"	# Ici, le poste local 176.130.194.32, 192.168.0.33
    port = 4212	# Se connecter sur le port 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    message = "Moi"
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    monIP = reponse.decode("utf-8")
    print("Connexion au serveur effectuée")
    
connexionserveur()
print("Bonjour,")
print("Merci de laisser votre avis")
print("Que voulez vous dire")
action = input(" ")
action = "Avis" + action
client.send(action.encode("utf-8"))
print("Merci!")
sleep(2)