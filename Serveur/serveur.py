#   Author  :   Adrien LD
#   Date    :   26/10/2021
#   Desc    :   Server - Ultimate Buvery


from random import *
import socket
import threading
import os
from math import *
from time import*
from datetime import datetime


threadsClients = []
Serveursclients = []
clients = []
version = '0.1.0'

def instanceServeur (client, infosClient):
    global version
    adresseIP = infosClient[0]
    port = str(infosClient[1])
    print("Instance de serveur prêt pour " + adresseIP + ":" + port)
    message = ""
    while message.upper() != "FIN":
        print(Serveursclients)
        message = client.recv(255).decode("utf-8")
        print(message)
        if message == "nouvI":
            alea = randrange ( 100, 999, 1)
            while Serveursclients.count(alea):
                alea = randrange ( 100, 999, 1)
            client.send(str(alea).encode("utf-8"))
            Serveursclients.append([adresseIP, alea,[adresseIP, 16, 0, " ", -1, 0]])
            print(Serveursclients)
        elif message.find("IP") != -1 : 
            renvoi = '0'
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    if Serveursclients[i][j][0] == str(adresseIP):
                        del Serveursclients[i][j]
            for i in range (len(Serveursclients)):
                if Serveursclients[i][1] == int(message.removeprefix("IP")):
                    Serveursclients[i].append([adresseIP, 16, 0, " ", -1, 0])
                    renvoi = '1'
                    print(Serveursclients)
            client.send(renvoi.encode("utf-8"))
        elif message.find("NAME") != -1 :
            print("on est ici", len(Serveursclients))
            deja = 0
            for i in range (len(Serveursclients)):
                for j in range (2,len(Serveursclients[i])):
                    if Serveursclients[i][j][0] == str(adresseIP):
                        for h in range(2,len(Serveursclients[i])):
                            if Serveursclients[i][h][3] == message.removeprefix("NAME"):
                                print("Le nom : ", message.removeprefix("NAME"), " de ", adresseIP, " est déjà utilisé par : ", Serveursclients[i][h][0])
                                deja = 1
                        if deja == 0:
                            Serveursclients[i][j][3] = message.removeprefix("NAME")
            client.send(str(deja).encode("utf-8"))
            print(Serveursclients)
        elif message == 'Infoteam':
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    #print (type(Serveursclients[i][j][0]), "et aussi ", type(adresseIP))
                    if Serveursclients[i][j][0] == adresseIP:
                        #print("Envoi de :", str(Serveursclients[i]))
                        client.send(str(Serveursclients[i]).encode("utf-8"))
        elif message.find("Round") != -1:
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    if Serveursclients[i][j][0] == adresseIP:
                        Serveursclients[i][j][4] = int(message.removeprefix("Round"))
                        print(Serveursclients[i])
        elif message.find("Age") != -1:
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    if Serveursclients[i][j][0] == adresseIP:
                        Serveursclients[i][j][1] = int(message.removeprefix("Age"))
                        print(Serveursclients[i])
        elif message.find("Equipe") != -1:
            joueur = ''
            selection = 1
            stop = 0
            message = message.removeprefix("Equipe")
            for i in range (len(message)):
                if message[i] != ' ' and stop == 0:
                    joueur += message[i]
                elif stop == 0:
                    team = int(message[i+1])
                    stop = 1
            joueur = int(joueur)
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    if Serveursclients[i][j][5] == team:
                        if selection == joueur:
                            if Serveursclients[i][j][5] == 0:
                                Serveursclients[i][j][5] = 1
                            elif Serveursclients[i][j][5] == 1:
                                Serveursclients[i][j][5] = 0
                        else : selection += 1
            print("J&T : ", joueur, team)
        elif message == 'Moi':
            client.send(str(adresseIP).encode("utf-8"))
        elif message == 'Version':
            client.send(version.encode("utf-8"))
        elif message == 'MAJ':
            derniereversion = (version + ".tar")
            fichier = open(derniereversion, 'rb')
            taille = os.path.getsize(derniereversion)/1024
            print(">Transfert de ", derniereversion, ' de taille ', taille, 'Ko')
            print("Nom fichier ", str(derniereversion), " taille ", str(taille))
            taille = taille * 1024
            print(taille)
            sleep(.5)
            num = 0
            pourcent = 0
            if isinstance(taille/1024, float):taille = ceil (taille/1024)+1
            else : taille = taille /1024
            for i in range (taille):
                fichier.seek(num, 0)
                donnees = fichier.read(1024)
                client.send(donnees)
                num += 1024
                
                if pourcent == 0 and num > taille / 100 * 10 and num < taille / 100 * 20:
                    print (" >> 10%")
                    pourcent = 1
                elif pourcent == 1 and num > taille / 100 * 20 and num < taille / 100 * 30:
                    print (" >> 20%")
                    pourcent = 2
                elif pourcent < 3 and num > taille / 100 * 30 and num < taille / 100 * 40:
                    print (" >> 30%")
                    pourcent = 3
                elif pourcent < 4 and num > taille / 100 * 40 and num < taille / 100 * 50:
                    print (" >> 40%")
                    pourcent = 4
                elif pourcent < 5 and num > taille / 100 * 50 and num < taille / 100 * 60:
                    print (" >> 50%")
                    pourcent = 5
                elif pourcent < 6 and num > taille / 100 * 60 and num < taille / 100 * 70:
                    print (" >> 60%")
                    pourcent = 6
                elif pourcent < 7 and num > taille / 100 * 70 and num < taille / 100 * 80:
                    print (" >> 70%")
                    pourcent = 7
                elif pourcent < 8 and num > taille / 100 * 80 and num < taille / 100 * 90:
                    print (" >> 80%")
                    pourcent = 8
                elif pourcent < 9 and num > taille / 100 * 90 and num < taille / 100 * 100:
                    print (" >> 90%" )                   
                    pourcent = 9
            
            sleep(.5)
            client.send(b"Fin")
            print("Envoi terminé")
        elif message.find("NEWV") != -1:
            if adresseIP == '82.66.94.198':
                message = message.removeprefix("NEWV")
                version = message
                print (version)
        elif message == "Taille":
            derniereversion = (version + ".tar")
            fichier = open(derniereversion, 'rb')
            taille = os.path.getsize(derniereversion)
            client.send(str(taille).encode('utf-8'))
            fichier.close()
        elif message == "quit":
            for i in range (len(Serveursclients)):
                for j in range (2, len(Serveursclients[i])):
                    if Serveursclients[i][j][0] == adresseIP:
                        print("On supprime l'utilisateur : ", adresseIP, i, j)
                        print(Serveursclients[i], Serveursclients[i][j])
                        if j == 2:
                            del Serveursclients[i]
                        else :
                            del Serveursclients[i][j]
                        print("Suppression réussie")
                        print(Serveursclients)
        elif message.find("Avis") != -1:
            fichier = open("Avis.txt", "a")
            fichier.write(adresseIP)
            fichier.write("\n")
            fichier.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            fichier.write("\n")
            fichier.write(message.removeprefix("Avis"))
            fichier.write("\n\n\n")
            fichier.close()

        




    print("Connexion fermée avec " + adresseIP + ":" + port)
    client.close()
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 4212))	# Écoute sur le port 50000
serveur.listen(5)
while True:
    client, infosClient = serveur.accept()
    clients.append(client)
    threadsClients.append(threading.Thread(None, instanceServeur, None, (client, infosClient), {}))
    threadsClients[-1].start()
serveur.close()