from time import *
from random import *
import socket
import tarfile
import sys
import os
import shutil
client = ''


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

def main1():
    connexionserveur()
    global version
    fichier1 = open ("Images/version.txt", 'r')
    version = fichier1.read()
    fichier1.close()
    print(version)
    client.send('Version'.encode("utf-8"))
    nouvelleversion = client.recv(255)
    nouvelleversion = nouvelleversion.decode("utf-8")
    print (nouvelleversion)
    sleep(.5)
    if nouvelleversion != version:
        message = "NEWV" + str(version)
        client.send(message.encode("utf-8"))


def versionchercheur():
    connexionserveur()
    global version, installation
    try :
        fichier1 = open ("Images/version.txt", 'r')
        version = fichier1.read()
        fichier1.close()
        client.send('Version'.encode("utf-8"))
        reponse = client.recv(255)
        reponse = reponse.decode("utf-8")
        if reponse != version:
            installation = 1
            main()
    except FileNotFoundError:
        client.send('Version'.encode("utf-8"))
        reponse = client.recv(255)
        version = reponse.decode("utf-8")
        installation = 0
        main()
    
    print(version)
    import test
    sys.exit()

def main():
    client.send('MAJ'.encode("utf-8"))
    nomfichier = version + '.tar'
    fichier = open(nomfichier, 'wb')
    fichier.close()
    print("Demande du nouveau fichier")
    reception = b""
    nombre = 0
    fichier = open(nomfichier, 'ab')
    while reception != b'Fin':
        fichier.write(reception)
        reception = client.recv(1024)
        nombre += len(reception)
        #print(taille, nombre)
    fichier.close()
    client.close()
    if installation:
        os.remove('test.py')
        shutil.rmtree('Images')
    print("Fichier bien reçu, Fichiers antérieurs supprimés")
    with tarfile.open(nomfichier, "r:") as tar:
        tar.extractall()
        tar.close()
    print("fichier décompréssé")
    os.remove(nomfichier)
    

main1()
#versionchercheur()