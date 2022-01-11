#   Author  :   Adrien LD
#   Date    :   26/10/2021
#   Desc    :   Ultimate Buvery

from tkinter import * 
from PIL import Image, ImageTk
from time import *
from random import *
import socket
import ast
import threading

version = ''
#Il y a écrit 2
window = Tk()
window.title ('CHOIX AGENT')

l = 1706
h = 720
canvas = 2
shieldchoix = 0
prix = 1000
nouvprix = 0
round = 1

fenetre1 = Canvas (window, width = l, height = h, bg = "black",highlightbackground="black")
fenetre1.pack(padx = 0, pady = 0)
window.iconbitmap('Images/Dé v1.ico')
activerclic = 1
coulbouttons = '#000066'
ancienchoix = 0
choix = 17
alea = 0
couleursagents = ['#8c978f', '#0e1821', '#ece8e2', '#ef3055', '#ff4753', '#161a25', '#fe4854', '#ebe7e1', '#0e1821', '#ece8e2', '#e7294e', '#ece8e2', '#0e1821', '#0e1821', '#0e1821', '#0d1423']
armeslegeres = ['Classic','Shorty','Frenzy','Ghost','Sheriff', 'Stinger','Spectre','Bulldog','Guardian','Phantom','Vandal','Bucky','Judge','Marshal','Operator','Ares','Odin']
prixlegeres = [0, 200, 400, 500, 800,1000,1600,2100, 2700, 2900, 2900, 900, 1500, 1100, 4500, 1700, 3200]
shields = ['Rien', 'Leger','Lourd']
prixshields = [0, 400, 1000]
agents = ['Astra', 'Breach', 'Brimstone', 'Cypher', 'Jett', 'Kayio', 'Killjoy', 'Omen', 'Phoenix','Raze','Reyna','Sage','Skye', 'Sova','Viper','Yoru','','']
competences = [
[],
["Replique", "200", "1" , "0", "Point d'ignition" ,"250","2", "0"],
["Balise stimulante", "100", "2" , "0", "Bombe incendiaire" ,"250","1", "0", "Frappe fumigène" ,"100","3", "0"],
["Fil de détente", "200", "2" , "0", "Cybercage" ,"100","2", "0"],
["Averse", "200", "2" , "0", "Courant Ascendant" ,"150","2", "0"],
["Fragment", "200", "1" , "0", "Mémoire flash" ,"250","2", "0"],
["Essaim de nanites", "200", "2" , "0", "Bot-alarme" ,"200","1", "0"],
["Paranoia", "300", "1" , "0", "Voile sombre" ,"100","2", "0", "Voie des ombres" ,"150","2", "0"],
["Brasier", "200", "1" , "0", "Balle courbe" ,"250","2", "0"],
["Boom bot", "300", "1" , "0", "Pack explosif" ,"200","2", "0"],
["Oeillade", "200", "2" , "0", "Dévoration" ,"200","2", "0"],
["Orbe barrière", "400", "1" , "0", "Orbe de lanteur" ,"200","2", "0"],
["Revitalisation", "200", "1" , "0", "Éclaireur" ,"250","1", "0", "Guide Éclatant" ,"250","2", "0"],
["Drone rapace", "400", "1" , "0", "Électroflèche" ,"150","2", "0"],
["Morsure du serpent", "200", "2" , "0", "Nuage de poison" ,"200","1", "0"],
["Feinte", "100", "2" , "0", "Angle mort" ,"250","2", "0"]
]
agnetsnonchoisis = []
agentschoisisparequipe = []
taillecarre= 5
ouvert = 16
agent = 17
armechoix = 0
competencestotales = 0
demander1, demander2, demander3 = 0, 0, 0
retre = 10
couleurb3 = 'green'
compx, compc = -10,-10
reponseserv ='0'
nommulti = ''
caseentrable = 0
equipe, mateam= [], []
sortirbouclenoms, ancienouvert, multijoueur, maitredujeu ,monIP =1, 0 , 0, 0, ''
BouttonOFF, loop = 0, 0

try :
    nom = open("nom.txt", "r")
    nommulti = nom.readline()
    nom.close()
except :
    print("Fichier ouvert")


def versionchercheur():
    global version
    fichier = open("Images/version.txt", 'r')
    version = fichier.read()
    fichier.close()
    print(version)

def dimensionnertout():
    global tailleimagex, MAJx, MAJc, tailleimagey, nomagentx , nomagenty, nomagentc, nomagentu, prixx , prixy, prixc, prixu, roundx, roundy, roundc, roundu, armex, armey, armec, armeu, shieldx, shieldy, shieldc, shieldu, haut1, haut2, aleax, aleay, aleac, aleau, validerx, validery, validerc, valideru, retourx, retoury, retourc, retouru, creerservx, creerservy, creerservc, creerservu, joinservx, joinservc, solox, soloc
    tailleimagex, tailleimagey = int(l/8-retre), int((l/8-retre)/1.785)
    nomagentx , nomagenty, nomagentc, nomagentu = 8*l/16, 0.5*h/18, 14*l/16, 2.5*h/18
    prixx , prixy, prixc, prixu = 12*l/16, 15.5*h/18, 15*l/16, 17.5*h/18
    roundx, roundy, roundc, roundu = 9*l/16, 2.9*h/18, 13*l/16, 4.4*h/18
    armex, armey, armec, armeu = 7*l/16, 5*h/18, 10*l/16, 7*h/18
    shieldx, shieldy, shieldc, shieldu = 12*l/16, 5*h/18, 15*l/16, 7*h/18
    
    aleax, aleay, aleac, aleau = 1*l/6, 15*h/18, 2*l/6, 17*h/18
    validerx, validery, validerc, valideru = 4*l/6, 15*h/18, 5*l/6, 17*h/18
    retourx, retoury, retourc, retouru = 7*l/16, 15.5*h/18, 10*l/16, 17.5*h/18
    creerservx, creerservy, creerservc, creerservu = 1.5*l/16, 8*h/18, 5*l/16, 10*h/18
    joinservx, joinservc= 6*l/16, 10*l/16
    solox, soloc = 11*l/16, 14.5*l/16
    MAJx, MAJc = 0.5*l/16, 4.5*l/16

def creercanvas():
    global OFF
    fenetre1.delete(ALL)
    changerfond()
    if canvas == 1:creercanvas1()
    elif canvas == 2:creercanvas2()
    elif canvas == 3:creercanvas3()
    elif canvas == 4:creercanvas4()
    else:creercanvas0()
    if BouttonOFF :OFF = Image.open ( 'Images/Supplement/OFF(1).png')
    else : OFF = Image.open ( 'Images/Supplement/OFF.png')
    OFF = OFF.resize((int(h/12),int(h/12)))
    OFF = ImageTk.PhotoImage(OFF)
    fenetre1.create_image((int(l-h/12),int(h/12)), image=OFF)
    fenetre1.update()

def connexionserveur():
    global client, monIP
    adresseIP = "176.130.194.32"	# Ici, le poste local 176.130.194.32, 192.168.0.33
    port = 4212	# Se connecter sur le port 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    message = "Moi"
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    monIP = reponse.decode("utf-8")
    print("Connexion au serveur effectuée")
    return 1

def affichercompetences():
    global comp1,comp2,comp3, comp4, comp5, comp6, compet1, compet2, compet3, compet4, compet5, compet6, competencestotales
    if len(competences[agent])/4 == 0:
        competencestotales = 0
    if len(competences[agent])/4 >= 1:
        comp = Image.open ('Images/competences/' + competences[agent][0] + '.png')
        comp = comp.resize((int(h/8),int(h/8)))
        comp1 = ImageTk.PhotoImage(comp) 
        comp = Image.open ('Images/competences/' + competences[agent][2] + "." + competences[agent][3] + "." + str(demander1) + '.png')
        comp = comp.resize((int(h/5),int((h/5)/5.2)))
        comp4 = ImageTk.PhotoImage(comp) 
        compet1 = fenetre1.create_image((l/6, h/2), image=comp1)
        compet4 = fenetre1.create_image((int(10*l/16),int(12.5*h/16)), image=comp4)
    if len(competences[agent])/4 >= 2:
        fenetre1.delete(compet1)
        fenetre1.delete(compet4)
        comp = Image.open ('Images/competences/' + competences[agent][4] + '.png')
        comp = comp.resize((int(h/8),int(h/8)))
        comp2 = ImageTk.PhotoImage(comp) 
        comp = Image.open ('Images/competences/' + competences[agent][6] + "." + competences[agent][7] + "." + str(demander2) + '.png')
        comp = comp.resize((int(h/5),int((h/5)/5.2)))
        comp5 = ImageTk.PhotoImage(comp) 
        compet4 = fenetre1.create_image((int(10*l/16),int(12.5*h/16)), image=comp4)
        compet5 = fenetre1.create_image((int(12*l/16),int(12.5*h/16)), image=comp5)
        compet1 = fenetre1.create_image((int(10*l/16),int(11*h/16)), image=comp1)
        compet2 = fenetre1.create_image((int(12*l/16),int(11*h/16)), image=comp2)
        competencestotales = 2
    if len(competences[agent])/4 >= 3:
        fenetre1.delete(compet1)
        fenetre1.delete(compet2)
        fenetre1.delete(compet4)
        fenetre1.delete(compet5)
        comp = Image.open ('Images/competences/' + competences[agent][8] + '.png')
        comp = comp.resize((int(h/8),int(h/8)))
        comp3 = ImageTk.PhotoImage(comp) 
        comp = Image.open ('Images/competences/' + competences[agent][10] + "." + competences[agent][11] + "." + str(demander3) + '.png')
        comp = comp.resize((int(h/5),int((h/5)/5.2)))
        comp6 = ImageTk.PhotoImage(comp) 
        compet4 = fenetre1.create_image((int(9.2*l/16),int(12.5*h/16)), image=comp4)
        compet5 = fenetre1.create_image((int(11*l/16),int(12.5*h/16)), image=comp5)
        compet6 = fenetre1.create_image((int(12.8*l/16),int(12.5*h/16)), image=comp6)
        compet1 = fenetre1.create_image((int(9.2*l/16),int(11*h/16)), image=comp1)
        compet2 = fenetre1.create_image((int(11*l/16),int(11*h/16)), image=comp2)
        compet3 = fenetre1.create_image((int(12.8*l/16),int(11*h/16)), image=comp3)
        competencestotales = 3
    
def bouton(x,y,c,u, text, coul):
    diam = min( (c-x),(u-y))/5
    diamm = (diam/2)
    fenetre1.create_oval(x,y,x+diam,y+diam,fill=coul, outline='')
    fenetre1.create_oval(c,u,c-diam,u-diam,fill=coul, outline='')
    fenetre1.create_oval(x,u,x+diam,u-diam,fill=coul, outline='')
    fenetre1.create_oval(c,y,c-diam,y+diam,fill=coul, outline='')
    fenetre1.create_rectangle((x+diamm, y),(c-diamm,u+1),fill=coul, outline='')
    fenetre1.create_rectangle((x, y+diamm),(c+1,u-diamm),fill=coul, outline='')
    fenetre1.create_text((x+c)/2, (y+u)/2, text = text, fill = "white", font="Arial 40")

def bouton3(x,y,c,u):
    fenetre1.create_rectangle(x,y,c,u,fill = '#5c6d82', outline = '')
    
    fenetre1.create_rectangle(x+taillecarre,y+taillecarre,c-taillecarre,u-taillecarre,fill = '#8390a1', outline = '')
    
    fenetre1.create_rectangle(x+taillecarre+taillecarre/3,y+taillecarre+taillecarre/3,c-taillecarre-taillecarre/3,u-taillecarre-taillecarre/3,fill = couleursagents[agent], outline = '')
    fenetre1.create_rectangle(compx+taillecarre+taillecarre/3, int(9.7*h/16)+taillecarre+taillecarre/3, compc-taillecarre-taillecarre/3, int(13.1*h/16)-taillecarre-taillecarre/3, fill = '#646a13', outline = '')
    fenetre1.create_rectangle(x,y,x+taillecarre,y+taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(x,u,x+taillecarre,u-taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(c,y,c-taillecarre,y+taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(c,u,c-taillecarre,u-taillecarre, fill = 'white', outline = '')

def bouton2(x,y,c,u, text):
    fenetre1.create_rectangle(x,y,c,u,fill = '#5c6d82', outline = '')
    fenetre1.create_rectangle(x+taillecarre,y+taillecarre,c-taillecarre,u-taillecarre,fill = '#8390a1', outline = '')
    fenetre1.create_rectangle(x+taillecarre+taillecarre/3,y+taillecarre+taillecarre/3,c-taillecarre-taillecarre/3,u-taillecarre-taillecarre/3,fill = '#5c6d82', outline = '')
    fenetre1.create_rectangle(x,y,x+taillecarre,y+taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(x,u,x+taillecarre,u-taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(c,y,c-taillecarre,y+taillecarre, fill = 'white', outline = '')
    fenetre1.create_rectangle(c,u,c-taillecarre,u-taillecarre, fill = 'white', outline = '')
    fenetre1.create_text(((x+c)/2)+1, ((y+u)/2)+1, text = text, fill = "black", font="Bahnschrift 22")
    fenetre1.create_text((x+c)/2, (y+u)/2, text = text, fill = "white", font="Bahnschrift 22")

def boutoncompetences():
    if len(competences[agent])/4 == 1:
        bouton3(int(10*l/16),int(10*h/16),int(10*l/16),int(10*h/16))
    elif len(competences[agent])/4 == 2:
        bouton3(int(9.2*l/16),int(9.7*h/16),int(10.8*l/16),int(13.1*h/16))
        bouton3(int(11.2*l/16),int(9.7*h/16),int(12.8*l/16),int(13.1*h/16))
    elif len(competences[agent])/4 == 3:
        bouton3(int(8.4*l/16),int(9.7*h/16),int(10*l/16),int(13.1*h/16))
        bouton3(int(10.2*l/16),int(9.7*h/16),int(11.8*l/16),int(13.1*h/16))
        bouton3(int(12*l/16),int(9.7*h/16),int(13.6*l/16),int(13.1*h/16))

def creercanvas1():
    global arme2,shield2, fond, fond2
    fond = Image.open ('Images/Presentation/' + str(agents[agent]) + '.gif')
    larg,haut = fond.size
    fond = fond.resize((int((h)*(larg/haut)),int(h)))
    fond2 = ImageTk.PhotoImage(fond) 
    fenetre1.create_image((l/6, h/2), image=fond2)
    fenetre1.create_rectangle(compx, int(9.8*h/16), compc, int(13*h/16), fill = couleurb3)
    arme = Image.open ( 'Images/Armes/' + str(armeslegeres[armechoix]) + '.png')
    larg, haut = arme.size
    arme = arme.resize((int((h/8)*(larg/haut)), int(h/8)))
    arme2 = ImageTk.PhotoImage(arme)
    fenetre1.create_image((8.5*l/16, 9*h/18), image=arme2)
    shield = Image.open('Images/Armes/' + str(shields[shieldchoix]) + '.gif')
    shield = shield.resize((int(h/6), int(h/6)))
    shield2 = ImageTk.PhotoImage(shield)
    fenetre1.create_image((13.5*l/16, 9*h/18), image=shield2)
    boutoncompetences()
    affichercompetences()
    bouton2(armex, armey, armec, armeu, armeslegeres[armechoix].upper())
    bouton2(shieldx, shieldy, shieldc, shieldu, shields[shieldchoix].upper())
    bouton2(retourx, retoury, retourc, retouru, "RETOUR")
    bouton2(nomagentx , nomagenty, nomagentc, nomagentu, str(agents[agent]).upper())
    bouton2(roundx, roundy, roundc, roundu, "ROUND : " + str(round) )
    if prix == 0:
        bouton2(prixx , prixy, prixc, prixu, 'ARGENT')
    else :
        bouton2(prixx , prixy, prixc, prixu, str(prix))

def creercanvas0():
    global fond2, haut1, haut2
    if multijoueur :
        haut1, haut2 = h/3.7, h/2.2
    else :
        haut1, haut2 = h/2.5, h/1.7
    fond = Image.open ( 'Images/Fond4.gif')
    fond = fond.resize((l,h))
    fond2 = ImageTk.PhotoImage(fond)
    fenetre1.create_image((l/2, h/2), image=fond2)
    
    if alea == 0:
        bouton2(l/6, h/18, 5*l/6, 3*h/18, "CHOISISSEZ VOTRE AGENT")
    elif alea == 1:
        bouton2(l/6, h/18, 5*l/6, 3*h/18, "INDIQUEZ LES AGENTS QUE VOUS N'AVEZ PAS")
    bouton2(validerx, validery,validerc,valideru, "VALIDER")
    bouton2(aleax, aleay,aleac,aleau, "ALEATOIRE")
    imagesagents()
    if multijoueur :
        afficherchoixequipeecran0()

def creercanvas2():
    global fond2
    fond = Image.open ( 'Images/Fond4.gif')
    fond = fond.resize((l,h))
    fond2 = ImageTk.PhotoImage(fond)
    fenetre1.create_image((l/2, h/2), image=fond2)
    bouton2(l/6, h/18, 5*l/6, 3*h/18, "CHOISISSEZ VOTRE MODE DE CONNEXION")
    bouton2(creerservx, creerservy, creerservc, creerservu, "CREER SERVEUR")
    bouton2(joinservx, creerservy, joinservc, creerservu, "REJOINDRE SERVEUR")
    bouton2(solox, creerservy, soloc, creerservu, "SOLO")
    texte = "V."+ version
    fenetre1.create_text(15.5*l/16, 17.5*h/18, text = texte, fill = "white", font="Bahnschrift 16")
    fenetre1.create_text(1.5*l/16, 17.5*h/18, text = "By G6®, SpaceBirdZ, U_B_Valo©", fill = "white", font="Bahnschrift 16")

def creercanvas3():
    global fond2, requeteserveur, client, IPserveur
    fond = Image.open ( 'Images/Fond4.gif')
    fond = fond.resize((l,h))
    fond2 = ImageTk.PhotoImage(fond)
    fenetre1.create_image((l/2, h/2), image=fond2)
    bouton2(solox, validery, soloc, valideru, "VALIDER")
    bouton2(creerservx, validery, creerservc, valideru, "RETOUR")
    if caseentrable == 2:
        bouton2(l/6, h/18, 5*l/6, 3*h/18, "ENTREZ VOTRE PSEUDO")
        if nommulti == '':bouton2(joinservx, creerservy, joinservc, creerservu, "PSEUDO")
        else :bouton2(joinservx, creerservy, joinservc, creerservu, nommulti)
    else:
        bouton2(l/6, h/18, 5*l/6, 3*h/18, "VOICI VOTRE MDP DE CONNEXION")
        bouton2(joinservx, creerservy, joinservc, creerservu, str(IPserveur))
        
        utiuliserlisteequipes()

def creercanvas4():
    global fond2, requeteserveur, client, IPserveur, validerIP, reponseserv
    fond = Image.open ( 'Images/Fond4.gif')
    fond = fond.resize((l,h))
    fond2 = ImageTk.PhotoImage(fond)
    fenetre1.create_image((l/2, h/2), image=fond2)
    bouton2(solox, validery, soloc, valideru, "VALIDER")
    bouton2(creerservx, validery, creerservc, valideru, "RETOUR")
    bouton2(l/6, h/18, 5*l/6, 3*h/18, "CONNEXION SERVEUR")
    if IPserveur == 0:bouton2(creerservx, creerservy, joinservx, creerservu, "SERVEUR")
    else :bouton2(creerservx, creerservy, joinservx, creerservu, str(IPserveur))
    if nommulti == '':bouton2(joinservc, creerservy, soloc, creerservu, "PSEUDO")
    else :bouton2(joinservc, creerservy, soloc, creerservu, nommulti)
    if caseentrable == 1:
        if IPserveur == 0:agrandirbouton2(creerservx, creerservy, joinservx, creerservu, "SERVEUR")
        else :agrandirbouton2(creerservx, creerservy, joinservx, creerservu, str(IPserveur))
    elif caseentrable == 2:
        if nommulti == '':agrandirbouton2(joinservc, creerservy, soloc, creerservu, "PSEUDO")
        else :agrandirbouton2(joinservc, creerservy, soloc, creerservu, nommulti)
        

class MonThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while (loop):
            global equipe, canvas, sortirbouclenoms, ancienneequipe
            ancienneequipe = equipe
            equipe = recupererinfosequipe()
            print (equipe)
            if canvas == 3 and ancienneequipe != equipe:
                creercanvas()
                utiuliserlisteequipes()
            elif canvas == 0:
                afficherchoixequipeecran0()
            sleep(1)
        print("finloop")

def afficherchoixequipeecran0():
    global imagesagentsj1, imagesagentsj2, imagesagentsj3, imagesagentsj4
    hautimage, hautnom = 11*h/16, 13*h/16
    if (len(mateam)) == 1:
        for i in range (2, len(equipe)):
            if equipe[i][0] == mateam [0]:
                imagesagentsj1 = Image.open ( "Images/Semiagents/"+ agents[equipe[i][1]] + "1.png")
                imagesagentsj1 = ImageTk.PhotoImage(imagesagentsj1)
                fenetre1.create_image((l/2, hautimage), image=imagesagentsj1)
                fenetre1.create_text(l/2, hautnom, text = equipe[i][3], fill = "white", font="Bahnschrift 16")

def recupererinfosequipe():
    message = "Infoteam"
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    reponseserv = reponse.decode("utf-8")
    equipe = ast.literal_eval(reponseserv.removeprefix('NAME'))
    return equipe

def utiuliserlisteequipes():
    global sortirbouclenoms, canvas
    for j in range (2, len(equipe)):
        if equipe[j][4] == 0 and sortirbouclenoms :
            print("On passe a l'écran suivant")
            canvas = 0
            envoyerround(0)
            trouvermonequipe()
            creercanvas()
            sortirbouclenoms = 0
        elif equipe[j][5] == 0:   
            fenetre1.create_text(3*l/16, (2*j*h/18)+(2*h/18), fill = '#3fabcc', text = equipe[j][3], font="Bahnschrift 25")
        elif equipe[j][5] == 1:   
            fenetre1.create_text(13*l/16, (2*j*h/18)+(2*h/18), fill = '#cc3f3f', text = equipe[j][3], font="Bahnschrift 25")

def actualiseragentschoisisequipe():
    global agentschoisisparequipe
    agentschoisisparequipe = []
    while canvas == 0:
        for j in range (2, len(equipe)):
            if equipe[j][1] != 16:
                agentschoisisparequipe.append(equipe[j][1])
        creercanvas()
    #print(agentschoisisparequipe)

def requetevaliderIPserveur():
    global IPserveur, canvas, caseentrable
    message = "IP" + str(IPserveur)
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    reponseserv = reponse.decode("utf-8")
    print("la")
    if reponseserv == '0':
        print("Serveur Invalide")
        IPserveur = 0
        canvas = 4
        caseentrable = 0
        creercanvas()
    else :
        requetenomserveur()
    print("reponse du serveur", reponseserv)

def requeteIPserveur():
    global IPserveur
    message = "nouvI"
    client.send(message.encode("utf-8"))
    print("Requete serveur envoyée afin d'obtenir le nom du serveur")
    reponse = client.recv(255)
    IPserveur = reponse.decode("utf-8")
    print("tout va bien")
    print("IP du serveur", IPserveur)

def requetenomserveur():
    global nommulti, canvas, caseentrable, loop
    print("requete nom serveur", nommulti)
    message = "NAME" + nommulti
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    reponse = reponse.decode("utf-8")
    print("ici")
    if reponseserv == '1':
        print("Nom Invalide")
        nommulti = ''
        canvas = 4
        caseentrable = 0
        creercanvas()
    else :
        print("Connexion bien établie avec le serveur")
        nom = open("nom.txt", "w")
        nom.write(nommulti)
        nom.close()
        loop = 1
        m = MonThread()
        m.start()
        creercanvas()

def envoyeragentchoisi(agent):
    if multijoueur:
        message = "Age" + str(agent)
        client.send(message.encode("utf-8"))

def envoyerround(round):
    global IPserveur
    if multijoueur:
        message = "Round" + str(round)
        client.send(message.encode("utf-8"))
        print("Envoi round 0")

def envoyerchangementequipe(joueur, rangée):
    print("requete changement equipe", joueur, rangée)
    message = "Equipe" + str(joueur-1) + " " + str(rangée)
    client.send(message.encode("utf-8"))
    print ("Joueur changé d'équipe")
    

def trouvermonequipe():
    global monequipe, mateam
    recupererinfosequipe()
    for j in range (2, len(equipe)):
        if equipe[j][0] == monIP:
            monequipe = equipe[j][5]
    for j in range (2, len(equipe)):
        if equipe[j][5] == monequipe:
            if equipe[j][0] != monIP:
                mateam.append(equipe[j][0])
    print("mateam", mateam)

def agrandirbouton2(x,y,c,u, text):
    coulbase1 = 95
    coulfin1 = 234
    coulbase2 = 112
    coulfin2 = 238
    coulbase3 = 135
    coulfin3 = 178
    coul1 = int((coulfin1-coulbase1)/14)
    coul2 = int((coulfin2-coulbase2)/14)
    coul3 = int((coulfin3-coulbase3)/14)
    ccoulbase1 = 89
    ccoulfin1 = 118
    ccoulbase2 = 106
    ccoulfin2 = 132
    ccoulbase3 = 129
    ccoulfin3 = 139
    ccoul1 = int((ccoulfin1-ccoulbase1)/14)
    ccoul2 = int((ccoulfin2-ccoulbase2)/14)
    ccoul3 = int((ccoulfin3-ccoulbase3)/14)
    ajout = taillecarre + taillecarre/3
    for i in range (14):
        fenetre1.create_rectangle(x,y,c,u,fill = "#{:x}{:x}{:x}".format(coulbase1+i*coul1,coulbase2+i*coul2,coulbase3+i*coul3), outline = '')
        fenetre1.create_rectangle(x+ajout,y+ajout,c-ajout,u-ajout,fill = "#{:x}{:x}{:x}".format(ccoulbase1+i*ccoul1,ccoulbase2+i*ccoul2,ccoulbase3+i*ccoul3), outline = '')
        fenetre1.create_rectangle(x+i,y+i,x+taillecarre+i,y+taillecarre+i, fill = 'white', outline = '')
        fenetre1.create_rectangle(x+i,u-i,x+taillecarre+i,u-taillecarre-i, fill = 'white', outline = '')
        fenetre1.create_rectangle(c-i,y+i,c-i-taillecarre,y+taillecarre+i, fill = 'white', outline = '')
        fenetre1.create_rectangle(c-i,u-i,c-i-taillecarre,u-i-taillecarre, fill = 'white', outline = '')
        fenetre1.create_text(((x+c)/2)+2, ((y+u)/2)+2, text = text, fill = "black", font="Bahnschrift 25")
        fenetre1.create_text((x+c)/2, (y+u)/2, text = text, fill = "white", font="Bahnschrift 25")
        fenetre1.update()
        sleep(.001)

def imagesagents():
    global haut1, haut2, a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17, b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17
    
    if agnetsnonchoisis.count(0) or agentschoisisparequipe.count(0):
        a0 = Image.open ( 'Images/Agents/Gris/' + agents[0] + '-1.gif')
    else:
        a0 = Image.open ( 'Images/Agents/' + agents[0] + '-1.gif')
    if agnetsnonchoisis.count(1) or agentschoisisparequipe.count(1):
        a1 = Image.open ( 'Images/Agents/Gris/' + agents[1] + '-1.gif')
    else:
        a1 = Image.open ( 'Images/Agents/' + agents[1] + '-1.gif')
    if agnetsnonchoisis.count(2) or agentschoisisparequipe.count(2):
        a2 = Image.open ( 'Images/Agents/Gris/' + agents[2] + '-1.gif')
    else:
        a2 = Image.open ( 'Images/Agents/' + agents[2] + '-1.gif')
    if agnetsnonchoisis.count(3) or agentschoisisparequipe.count(3):
        a3 = Image.open ( 'Images/Agents/Gris/' + agents[3] + '-1.gif')
    else:
        a3 = Image.open ( 'Images/Agents/' + agents[3] + '-1.gif')
    if agnetsnonchoisis.count(4) or agentschoisisparequipe.count(4):
        a4 = Image.open ( 'Images/Agents/Gris/' + agents[4] + '-1.gif')
    else:
        a4 = Image.open ( 'Images/Agents/' + agents[4] + '-1.gif')
    if agnetsnonchoisis.count(5) or agentschoisisparequipe.count(5):
        a5 = Image.open ( 'Images/Agents/Gris/' + agents[5] + '-1.gif')
    else:
        a5 = Image.open ( 'Images/Agents/' + agents[5] + '-1.gif')
    if agnetsnonchoisis.count(6) or agentschoisisparequipe.count(6):
        a6 = Image.open ( 'Images/Agents/Gris/' + agents[6] + '-1.gif')
    else:
        a6 = Image.open ( 'Images/Agents/' + agents[6] + '-1.gif')
    if agnetsnonchoisis.count(7) or agentschoisisparequipe.count(7):
        a7 = Image.open ( 'Images/Agents/Gris/' + agents[7] + '-1.gif')
    else:
        a7 = Image.open ( 'Images/Agents/' + agents[7] + '-1.gif')
    if agnetsnonchoisis.count(8) or agentschoisisparequipe.count(8):
        a8 = Image.open ( 'Images/Agents/Gris/' + agents[8] + '-1.gif')
    else:
        a8 = Image.open ( 'Images/Agents/' + agents[8] + '-1.gif')
    if agnetsnonchoisis.count(9) or agentschoisisparequipe.count(9):
        a9 = Image.open ( 'Images/Agents/Gris/' + agents[9] + '-1.gif')
    else:
        a9 = Image.open ( 'Images/Agents/' + agents[9] + '-1.gif')
    if agnetsnonchoisis.count(10) or agentschoisisparequipe.count(10):
        a10 = Image.open ( 'Images/Agents/Gris/' + agents[10] + '-1.gif')
    else:
        a10 = Image.open ( 'Images/Agents/' + agents[10] + '-1.gif')
    if agnetsnonchoisis.count(11) or agentschoisisparequipe.count(11):
        a11 = Image.open ( 'Images/Agents/Gris/' + agents[11] + '-1.gif')
    else:
        a11 = Image.open ( 'Images/Agents/' + agents[11] + '-1.gif')
    if agnetsnonchoisis.count(12) or agentschoisisparequipe.count(12):
        a12 = Image.open ( 'Images/Agents/Gris/' + agents[12] + '-1.gif')
    else:
        a12 = Image.open ( 'Images/Agents/' + agents[12] + '-1.gif')
    if agnetsnonchoisis.count(13) or agentschoisisparequipe.count(13):
        a13 = Image.open ( 'Images/Agents/Gris/' + agents[13] + '-1.gif')
    else:
        a13 = Image.open ( 'Images/Agents/' + agents[13] + '-1.gif')
    if agnetsnonchoisis.count(14) or agentschoisisparequipe.count(14):
        a14 = Image.open ( 'Images/Agents/Gris/' + agents[14] + '-1.gif')
    else:
        a14 = Image.open ( 'Images/Agents/' + agents[14] + '-1.gif')
    if agnetsnonchoisis.count(15) or agentschoisisparequipe.count(15):
        a15 = Image.open ( 'Images/Agents/Gris/' + agents[15] + '-1.gif')
    else:
        a15 = Image.open ( 'Images/Agents/' + agents[15] + '-1.gif')
    a0 = a0.resize((tailleimagex, tailleimagey))
    b0 = ImageTk.PhotoImage(a0)
    a1 = a1.resize((tailleimagex, tailleimagey))
    b1 = ImageTk.PhotoImage(a1)
    a2 = a2.resize((tailleimagex, tailleimagey))
    b2 = ImageTk.PhotoImage(a2)
    a3 = a3.resize((tailleimagex, tailleimagey))
    b3 = ImageTk.PhotoImage(a3)
    a4 = a4.resize((tailleimagex, tailleimagey))
    b4 = ImageTk.PhotoImage(a4)
    a5 = a5.resize((tailleimagex, tailleimagey))
    b5 = ImageTk.PhotoImage(a5)
    a6 = a6.resize((tailleimagex, tailleimagey))
    b6 = ImageTk.PhotoImage(a6)
    a7 = a7.resize((tailleimagex, tailleimagey))
    b7 = ImageTk.PhotoImage(a7)
    a8 = a8.resize((tailleimagex, tailleimagey))
    b8 = ImageTk.PhotoImage(a8)
    a9 = a9.resize((tailleimagex, tailleimagey))
    b9 = ImageTk.PhotoImage(a9)
    a10 = a10.resize((tailleimagex, tailleimagey))
    b10 = ImageTk.PhotoImage(a10)
    a11 = a11.resize((tailleimagex, tailleimagey))
    b11 = ImageTk.PhotoImage(a11)
    a12 = a12.resize((tailleimagex, tailleimagey))
    b12 = ImageTk.PhotoImage(a12)
    a13 = a13.resize((tailleimagex, tailleimagey))
    b13 = ImageTk.PhotoImage(a13)
    a14 = a14.resize((tailleimagex, tailleimagey))
    b14 = ImageTk.PhotoImage(a14)
    a15 = a15.resize((tailleimagex, tailleimagey))
    b15 = ImageTk.PhotoImage(a15)
    fenetre1.create_image(((0*l/8)+l/16, haut1), image= b0)
    fenetre1.create_image(((1*l/8)+l/16, haut1), image= b1)
    fenetre1.create_image(((2*l/8)+l/16, haut1), image= b2)
    fenetre1.create_image(((3*l/8)+l/16, haut1), image= b3)
    fenetre1.create_image(((4*l/8)+l/16, haut1), image= b4)
    fenetre1.create_image(((5*l/8)+l/16, haut1), image= b5)
    fenetre1.create_image(((6*l/8)+l/16, haut1), image= b6)
    fenetre1.create_image(((7*l/8)+l/16, haut1), image= b7)
    fenetre1.create_image(((0*l/8)+l/16, haut2), image= b8)
    fenetre1.create_image(((1*l/8)+l/16, haut2), image= b9)
    fenetre1.create_image(((2*l/8)+l/16, haut2), image= b10)
    fenetre1.create_image(((3*l/8)+l/16, haut2), image= b11)
    fenetre1.create_image(((4*l/8)+l/16, haut2), image= b12)
    fenetre1.create_image(((5*l/8)+l/16, haut2), image= b13)
    fenetre1.create_image(((6*l/8)+l/16, haut2), image= b14)
    fenetre1.create_image(((7*l/8)+l/16, haut2), image= b15)
    if choix != 16 and choix != 17:
        a16 = Image.open ( 'Images/Agents/Choix/' + agents[choix] + '-1.gif')
        a16 = a16.resize((tailleimagex, tailleimagey))
        if choix >= 8:
            choix2 = choix-8
            hauteur = haut2
        else :
            choix2 = choix
            hauteur = haut1
        b16 = ImageTk.PhotoImage(a16)
        fenetre1.create_image(((choix2*l/8)+l/16, hauteur), image= b16)

def agrandiragent(i):
    global agrandissement, imageagrandie
    if i>=8:
        v = i-8
        heuteur = haut2
    else :
        v=i
        heuteur = haut1
    j = 1
    if choix == i:
        agrandissement = Image.open ( 'Images/Agents/Choix/' + agents[i] + '-1.gif')
    elif agnetsnonchoisis.count(i):
        agrandissement = Image.open ( 'Images/Agents/Gris/' + agents[i] + '-1.gif')
    else:
        agrandissement = Image.open ( 'Images/Agents/' + agents[i] + '-1.gif')
    agrandissement = agrandissement.resize((tailleimagex+6*4, tailleimagey+6*4))
    imageagrandie = ImageTk.PhotoImage(agrandissement)
    fenetre1.create_image(((v*l/8)+l/16, heuteur), image= imageagrandie)
    fenetre1.update()
    j =j+1

def demarrerpartiemulti():
    global caseentrable, loop
    caseentrable = 1
    requeteIPserveur()
    requetenomserveur()
    loop = 1
    m = MonThread()
    m.start()
    creercanvas()

def agrandirimages(x,y):
    global ouvert, compx, compc, ancienouvert, BouttonOFF
    ancienouvert = ouvert
    global fond2, haut1, haut2
    if multijoueur :
        haut1, haut2 = h/3.7, h/2.2
    else :
        haut1, haut2 = h/2.5, h/1.7
    if x > int((l-h/12)-h/24) and x < int((l-h/12)+h/24) and y > int((h/12)-h/24) and y < int((h/12)+h/24):
        if ouvert != 30:
            BouttonOFF = 1
            ouvert = 30
            creercanvas()
            fenetre1.mainloop()
    elif ouvert == 30 : 
        BouttonOFF = 0
        ouvert = 16
    if canvas == 0:
        if y < (haut1-56):
            if ouvert != 16:
                ouvert = 16
        elif y<(haut1+56):
            for i in range (8):
                if x>(((i*l/8)+l/16)-100):
                    if x<(((i*l/8)+l/16)+100):
                        if ouvert != i:
                            ouvert = i
                            agrandiragent(i)
        elif y<(haut2+56):
            for i in range (8):
                if x>(((i*l/8)+l/16)-100):
                    if x<(((i*l/8)+l/16)+100):
                        if ouvert != i+8:
                            ouvert = i+8
                            agrandiragent(i+8)
        elif y < aleay:
            if ouvert != 16:
                ouvert = 16
        elif y < aleau :
            if x < aleax :
                ouvert = 16
            elif x < aleac :
                if ouvert != 17:
                    ouvert = 17
                    agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                    fenetre1.mainloop()
            elif x < validerx :
                ouvert = 16
            elif x < validerc:
                if ouvert != 18:
                    ouvert = 18
                    agrandirbouton2(validerx,validery ,validerc ,valideru, "VALIDER")
                    fenetre1.mainloop()
            else : 
                ouvert = 16
        else : 
            ouvert = 16
    elif canvas == 2:
        if y > creerservy and y < creerservu:
            if x > creerservx and x < creerservc:
                if ouvert != 19:
                    ouvert = 19
                    bouton2(creerservc, validery, solox, valideru, "HERBERGER SERVEUR PRIVE")
                    agrandirbouton2(creerservx, creerservy, creerservc, creerservu, "CREER SERVEUR")
                    fenetre1.mainloop()
            elif x > joinservx and x < joinservc:
                if ouvert != 20:
                    ouvert = 20
                    bouton2(creerservc, validery, solox, valideru, "REJOINDRE UN SERVEUR")
                    agrandirbouton2(joinservx, creerservy, joinservc, creerservu, "REJOINDRE SERVEUR")
                    fenetre1.mainloop()
            elif x > solox and x < soloc:
                if ouvert != 21:
                    ouvert = 21
                    bouton2(creerservc, validery, solox, valideru, "LANCER UNE PARTIE SOLO")
                    agrandirbouton2(solox, creerservy, soloc, creerservu, "SOLO")
                    fenetre1.mainloop()
            else : ouvert = 16
        else : ouvert = 16
    elif canvas == 3 or canvas == 4:
        if y > validery and y < valideru:
            if x > solox and x < soloc:
                if ouvert != 22:
                    ouvert = 22
                    agrandirbouton2(solox, validery, soloc, valideru, "VALIDER")
            elif x > creerservx and x < creerservc:
                if ouvert != 23:
                    ouvert = 23
                    agrandirbouton2(creerservx, validery, creerservc, valideru, "RETOUR")
            else : ouvert = 16
        elif canvas == 4 and y > creerservy and y < creerservu:
            if x > creerservx and x < joinservx:
                if ouvert != 19:
                    ouvert = 19
                    if IPserveur == 0:agrandirbouton2(creerservx, creerservy, joinservx, creerservu, "SERVEUR")
                    else :agrandirbouton2(creerservx, creerservy, joinservx, creerservu, str(IPserveur))
                    fenetre1.mainloop()
            elif x > joinservc and x < soloc:
                if ouvert != 18:
                    ouvert = 18
                    if nommulti == '':agrandirbouton2(joinservc, creerservy, soloc, creerservu, "PSEUDO")
                    else :agrandirbouton2(joinservc, creerservy, soloc, creerservu, nommulti)
                    fenetre1.mainloop()
            else : ouvert = 16
        else : ouvert = 16
    elif canvas == 1:
        compx, compc = -10,-10
        if y >= int(9.8*h/16) and y <= int(13*h/16):
            if len(competences[agent])/4 == 3 :
                if x >= int(8.4*l/16) and x <= int(10*l/16):
                    if ouvert != 25:
                        ouvert = 25
                        compx, compc = int(8.4*l/16),int(10*l/16)
                        creercanvas()
                elif x >= int(10.2*l/16) and x <= int(11.8*l/16):
                    if ouvert != 25:
                        ouvert = 25
                        compx, compc = int(10.2*l/16),int(11.8*l/16)
                        creercanvas()
                elif x >= int(12*l/16) and x <= int(13.6*l/16):
                    if ouvert != 25:
                        ouvert = 25
                        compx, compc = int(12*l/16), int(13.6*l/16)
                        creercanvas()
                else : ouvert = 16
            elif len(competences[agent])/4 == 2:
                if x >= int(9.2*l/16) and x <= int(10.8*l/16):
                    if ouvert != 25:
                        ouvert = 25
                        compx, compc = int(9.2*l/16), int(10.8*l/16)
                        creercanvas()
                elif x >= int(11.2*l/16) and x <= int(12.8*l/16):
                    if ouvert != 25:
                        ouvert = 25
                        compx, compc = int(11.2*l/16),int(12.8*l/16)
                        creercanvas()
                else: ouvert = 16
        elif y > retoury and y < retouru :
            if x > retourx and x < retourc :
                if ouvert != 19:
                    ouvert = 19
                    agrandirbouton2(retourx,retoury,retourc,retouru, "RETOUR")
                    fenetre1.mainloop()
            else :ouvert = 16
        else :ouvert = 16
    if ouvert == 16 and ancienouvert != ouvert:
        creercanvas()
    fenetre1.update()

def chargementaleatoire(age):
    enplus = 16
    epaisseur = 10
    if age > 7 :
        ageh = haut2
    else:
        ageh = haut1
    for i in range (8):
        if age == i or age == i+8:
            agel = (i*l/8)+l/16
    for i in range (int(tailleimagex/2)+enplus):
        fenetre1.create_line(int(agel), int(ageh - enplus - tailleimagey/2), int(agel +i), int(ageh - enplus - tailleimagey/2), fill = 'red', width = 10)
        fenetre1.update()
    for i in range (tailleimagey + enplus):
        fenetre1.create_line(int(agel + enplus + tailleimagex/2), int(ageh - enplus - tailleimagey/2 - epaisseur/2), int(agel + enplus + tailleimagex/2), int(ageh  - tailleimagey/2 + i ), fill = 'red', width = 10)
        fenetre1.update()
    for i in range (tailleimagex + enplus*2):
        fenetre1.create_line(int(agel + enplus + tailleimagex/2 + epaisseur/2), int(ageh + enplus + tailleimagey/2+2), int(agel + enplus + tailleimagex/2 -i), int(ageh + enplus + tailleimagey/2+2), fill = 'red', width = 10)
        fenetre1.update()
    for i in range (tailleimagey + enplus ):
        fenetre1.create_line(int(agel - enplus - tailleimagex/2 ), int(ageh + enplus + tailleimagey/2 + epaisseur/2 +2), int(agel - enplus - tailleimagex/2), int(ageh  + tailleimagey/2 - epaisseur/2 - i ), fill = 'red', width = 10)
        fenetre1.update()
    for i in range (tailleimagey + enplus):
        fenetre1.create_line(int(agel - tailleimagex/2 - enplus - epaisseur/2), int(ageh - enplus - tailleimagey/2), int(agel - tailleimagex/2 - enplus +i), int(ageh - enplus - tailleimagey/2), fill = 'red', width = 10)
        fenetre1.update()

def aleatoire():
    temps = 0.01
    rand1 = 0
    if len(agnetsnonchoisis) < 15:
        while temps < 0.4:
            rand = randint(0,15)
            while rand1 == rand:
                rand = randint(0,15)
            if  agnetsnonchoisis.count(rand) == 0:
                rand1 = rand
                agrandiragent(rand)
                temps = temps + temps*0.08
                sleep(temps)
        envoyeragentchoisi(rand)
        chargementaleatoire(rand)
    return rand

def tester():
    global armechoix, canvas, agent
    canvas = 1
    creercanvas
    for i in range (12):
        print(randrange(1))
    for i in range (len(agents)-2):
        agent = i
        creercanvas()
        sleep (.8)

def aleatoireshields(): 
    global prix, shieldchoix
    shieldchoix = randrange(len(shields)) 
    while prixshields[shieldchoix] > prix :
        shieldchoix = randrange(len(shields))
    prix = prix - prixshields[shieldchoix]

def aleatoirearmes():
    global armechoix, prix
    armechoix = randrange(len(armeslegeres))
    while prixlegeres[armechoix] > prix :
        armechoix = randrange(len(armeslegeres))
    prix = prix - prixlegeres[armechoix]

def aleatoirecomp():
    
    global prix, competences, demander1, demander2, demander3
    print(competences[agent], "et" , demander1, demander2, demander3)
    if len(competences[agent])/4 >= 1:
        nbrcomp1 = int(competences[agent][2])- int(competences[agent][3])
        aleacomp1 = randrange(nbrcomp1+1)
        while int(competences[agent][1])*aleacomp1 > prix  :
            aleacomp1 = randrange(nbrcomp1+1)
        demander1 = aleacomp1
        prix = prix - int(competences[agent][1])*aleacomp1
    if len(competences[agent])/4 >= 2:
        nbrcomp2 = int(competences[agent][6])- int(competences[agent][7])
        aleacomp2 = randrange(nbrcomp2+1)
        while int(competences[agent][5])*aleacomp2 > prix :
            aleacomp2 = randrange(nbrcomp2+1)
        demander2 = aleacomp2
        prix = prix - int(competences[agent][5])*aleacomp2
    if len(competences[agent])/4 >= 3:
        nbrcomp3 = int(competences[agent][10])- int(competences[agent][11])
        aleacomp3 = randrange(nbrcomp3+1)
        while int(competences[agent][9])*aleacomp3 > prix :
            aleacomp3 = randrange(nbrcomp3+1)
        demander3 = aleacomp3
        prix = prix - int(competences[agent][9])*aleacomp3
    print(competences[agent], "et" , demander1, demander2, demander3)

def aleatoire2():
    global prix
    aleaa = []
    aleatoireshields()
    aleatoirearmes()
    
    aleatoirecomp()
    prix = 0
    creercanvas()

def eteindretout():
    global loop 
    if multijoueur:
        client.send("quit".encode("utf-8"))
    loop=0
    window.destroy()
    print("OFF")
    client.close()

def touchepresee(event):
    global nouvprix, round, multijoueur,maitredujeu, IPserveur, caseentrable, prix, agent, canvas, choix, alea, ouvert, ancienchoix, demander1, demander2, demander3, nommulti
    ajout = event.keysym
    print(canvas, caseentrable)

    if canvas  == 1:
        if ajout == 'BackSpace':
            prix = int(prix / 10)
        elif ajout == 'Return':
            round = round + 1
            envoyerround(round)
            if len(competences[agent])/4 >= 1:
                competences[agent][3] = str(int(competences[agent][3]) + demander1)
            if len(competences[agent])/4 >= 2:
                competences[agent][7] = str(int(competences[agent][7]) + demander2)
            if len(competences[agent])/4 >= 3:
                competences[agent][11] = str(int(competences[agent][11]) + demander3)
            aleatoire2()
        elif ajout == 'a':
            tester()
        elif int(ajout):
            prix = prix * 10 + int(ajout)
        elif ajout == '0':
            prix = prix * 10 + int(ajout)
    elif canvas == 4:
        if ajout == 'Return':
            canvas = 3
            caseentrable = 3
            requetevaliderIPserveur()
    elif canvas == 2:
        creercanvas()
        if ajout == 'Return':
            if ouvert == 19:
                canvas = 3
                caseentrable = 2
                maitredujeu = 1
                multijoueur = 1
                if connexionserveur():print("Connexion serveur effectuée")
                else : print("Connexion serveur a échoué")
            elif ouvert == 20:
                canvas = 4
                multijoueur = 1
                IPserveur = 0
                if connexionserveur():print("Connexion serveur effectuée")
                else : print("Connexion serveur a échoué")
            elif ouvert == 21:
                canvas = 0
            creercanvas()
        if ajout == 'Right':
            if ouvert == 16 : ouvert = 19
            elif ouvert == 19 : ouvert = 20
            elif ouvert == 20 : ouvert = 21
            elif ouvert == 21 : ouvert = 19
            
        elif ajout == 'Left':
            if ouvert == 16 : ouvert = 21
            elif ouvert == 21 : ouvert = 20
            elif ouvert == 20 : ouvert = 19
            elif ouvert == 19 : ouvert = 21
        if ouvert == 19: 
            bouton2(creerservc, validery, solox, valideru, "HERBERGER SERVEUR PRIVE")
            agrandirbouton2(creerservx, creerservy, creerservc, creerservu, "CREER SERVEUR")
            fenetre1.mainloop()
        elif ouvert == 20: 
            bouton2(creerservc, validery, solox, valideru, "REJOINDRE UN SERVEUR")
            agrandirbouton2(joinservx, creerservy, joinservc, creerservu, "REJOINDRE SERVEUR")
            fenetre1.mainloop()
        elif ouvert == 21 : 
            bouton2(creerservc, validery, solox, valideru, "LANCER UNE PARTIE SOLO")
            agrandirbouton2(solox, creerservy, soloc, creerservu, "SOLO")
            fenetre1.mainloop()
    if caseentrable == 1:
        print(ajout, IPserveur)
        if ajout == 'BackSpace':
            IPserveur = int(IPserveur/10)
            creercanvas()
        if len(str(IPserveur)) < 3:
            if int(ajout):
                IPserveur = IPserveur * 10 + int(ajout)
            elif ajout == '0':
                IPserveur = IPserveur * 10 + int(ajout)
    elif caseentrable == 2:
        if ajout == 'BackSpace':
            if nommulti != '':
                nommulti = nommulti[:-1]
        if ajout == 'Return' and canvas == 3:
            demarrerpartiemulti()
        elif (event.keysym_num > 64 and event.keysym_num < 91) or (event.keysym_num > 96 and event.keysym_num < 123 ):
            if len(nommulti)<18:
                nommulti = nommulti + ajout
    elif canvas == 3 :
        if choix == 17:
            choix = 0
        elif ajout == 'Return':
            if choix < 16:
                agent = choix
                canvas = 1
                aleatoire2()
            elif choix == 16:
                sauvegarde = open("sauvegarde.txt", "w")
                for i in range (len(agnetsnonchoisis)):
                    sauvegarde.write(str(agnetsnonchoisis[i]) + "\n")
                sauvegarde.close()
                agent = aleatoire()
                canvas = 1
        elif ajout == 'Up':
            if choix < 16 and choix >7 and ouvert != 17:
                choix = choix-8
            elif ouvert == 17:
                ouvert = 16
            elif choix == 16:
                agnetsnonchoisis.clear()
                alea = 0
                choix = ancienchoix
        elif ajout == 'Right':
            if choix < 15 and choix >= 0:
                choix = choix+1
            elif choix == 15:
                if alea == 0:
                    ancienchoix = choix
                    choix = 16
                    alea = 1
                    sauve = open("sauvegarde.txt", "r")
                    theagnetsnonchoisis = sauve.readlines()
                    sauve.close()
                    for i in range (len (theagnetsnonchoisis)):
                        agnetsnonchoisis.append(int(theagnetsnonchoisis[i].strip('\n')))
                    creercanvas()
                    agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                    fenetre1.mainloop()
            elif choix == 16 :
                agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                fenetre1.mainloop()
        elif ajout == 'Left':
            if choix < 16 and choix > 0:
                choix = choix-1
            elif choix == 16:
                creercanvas()
                agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                fenetre1.mainloop()
        elif ajout == 'Down':
            if choix >= 0 and choix < 8:
                choix = choix+8
            elif  choix < 16:
                if alea == 0:
                    ancienchoix = choix
                    choix = 16
                    alea = 1
                    sauve = open("sauvegarde.txt", "r")
                    theagnetsnonchoisis = sauve.readlines()
                    sauve.close()
                    for i in range (len (theagnetsnonchoisis)):
                        agnetsnonchoisis.append(int(theagnetsnonchoisis[i].strip('\n')))
                    creercanvas()
                    agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                    fenetre1.mainloop()
            elif choix == 16 :
                agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                fenetre1.mainloop()

            
            
        elif int(ajout):
            prix = prix * 10 + int(ajout)
        elif ajout == '0':
            prix = prix * 10 + int(ajout)
    creercanvas()

def clic(event) : 
    x = event.x
    y = event.y
    global loop, round,  choix,ouvert,alea, IPserveur, maitredujeu, multijoueur, agnetsnonchoisis, agent, canvas, demander1, demander2, demander3, activerclic, requeteserveur, caseentrable
    if activerclic:
        print (canvas, x, y, retourx, retourc)
        if x > int((l-h/12)-h/24) and x < int((l-h/12)+h/24) and y > int((h/12)-h/24) and y < int((h/12)+h/24):
            eteindretout()
        if canvas == 0:
            if y<(haut1-56) : 
                choix = 16
            if y<(haut1+56) and y > haut1-56:
                for i in range (8):
                    if x>(((i*l/8)+l/16)-100) and x<(((i*l/8)+l/16)+100):
                        if alea == 1:
                            if agnetsnonchoisis.count(i):
                                agnetsnonchoisis.remove(i)
                            else :
                                agnetsnonchoisis.append(i)
                        elif choix != i:
                            choix = i
                            envoyeragentchoisi(choix)
            elif y<(haut2+56):
                for i in range (8):
                    if x>(((i*l/8)+l/16)-100) and x<(((i*l/8)+l/16)+100):
                        if alea == 1:
                            if agnetsnonchoisis.count(i+8):
                                agnetsnonchoisis.remove(i+8)
                            else :
                                agnetsnonchoisis.append(i+8)
                        elif choix != i+8:
                            choix = i+8
                            envoyeragentchoisi(choix)
            elif y < aleay:
                if choix != 16:
                    choix = 16
            elif y < aleau :
                if x < aleax :
                    choix = 16
                elif x < aleac :
                    if alea == 0:
                        choix = 16
                        alea = 1
                        sauve = open("sauvegarde.txt", "r")
                        theagnetsnonchoisis = sauve.readlines()
                        sauve.close()
                        for i in range (len (theagnetsnonchoisis)):
                            agnetsnonchoisis.append(int(theagnetsnonchoisis[i].strip('\n')))
                    elif choix == 16:
                        agnetsnonchoisis.clear()
                        alea = 0
                    creercanvas()
                    agrandirbouton2(aleax,aleay ,aleac ,aleau , "ALEATOIRE")
                    fenetre1.mainloop()
                elif x < validerx :
                    choix = 16
                elif x < validerc:
                    activerclic = 0
                    if alea == 1:
                        sauvegarde = open("sauvegarde.txt", "w")
                        for i in range (len(agnetsnonchoisis)):
                            sauvegarde.write(str(agnetsnonchoisis[i]) + "\n")
                        sauvegarde.close()
                        agent = aleatoire()
                    elif choix != 16:
                        agent = choix
                        envoyeragentchoisi(choix)
                    canvas = 1
                    activerclic = 1
                    aleatoire2()
                else : 
                    choix = 16
            else : 
                creercanvas()
                choix = 16
        elif canvas == 2 :
            if y > creerservy and y < creerservu:
                if x > creerservx and x < creerservc:
                    canvas = 3
                    multijoueur = 1
                    caseentrable = 2
                    maitredujeu = 1
                    if connexionserveur():print("Connexion serveur effectuée")
                    else : print("Connexion serveur a échoué")
                elif x > joinservx and x < joinservc:
                    canvas = 4
                    multijoueur = 1
                    IPserveur = 0
                    if connexionserveur():print("Connexion serveur effectuée")
                    else : print("Connexion serveur a échoué")
                elif x > solox and x < soloc:
                    canvas = 0
                else : ouvert = 16
            else : ouvert = 16
            creercanvas()
        elif canvas == 3 and maitredujeu == 1 :
            if caseentrable == 1:
                if x > 1*l/16 and x < 5*l/16:
                    for i in range (2, len(equipe)):
                        if y > (1.5*i*h/18)+(2*h/18) and y < (2.5*i*h/18)+(2*h/18):
                            envoyerchangementequipe(i, 0)
                elif x > 11*l/16 and x < 15*l/16:
                    for i in range (2, len(equipe)):
                        if y > (1.5*i*h/18)+(2*h/18) and y < (2.5*i*h/18)+(2*h/18):
                            envoyerchangementequipe(i, 1)
                if x > solox and x< soloc:
                    if y > validery and y < valideru:
                        if (len(equipe)) > 2:
                            envoyerround(0)
                        else :
                            print("Demarrage impossible, un seul joueur connecté")
                        
                if x > creerservx and x< creerservc:
                    if y > validery and y < valideru:
                        canvas = 2
                        creercanvas()
                        loop = 0
                        client.send("quit".encode("utf-8"))
                        multijoueur = 0
            elif caseentrable == 2:
                if x > creerservx and x< creerservc:
                    if y > validery and y < valideru:
                        canvas = 2
                        creercanvas()
                        loop = 0
                        multijoueur = 0
                elif x > solox and x< soloc:
                    if y > validery and y < valideru:
                        demarrerpartiemulti()
        elif canvas == 4:
            if  y > creerservy and y < creerservu:
                if x > creerservx and x < joinservx:
                    if caseentrable != 1:
                        caseentrable = 1
                        if IPserveur == 0:agrandirbouton2(creerservx, creerservy, joinservx, creerservu, "SERVEUR")
                        else :agrandirbouton2(creerservx, creerservy, joinservx, creerservu, str(IPserveur))
                        fenetre1.mainloop()
                elif x > joinservc and x < soloc:
                    if caseentrable != 2 :
                        caseentrable = 2
                        if nommulti == '':agrandirbouton2(joinservc, creerservy, soloc, creerservu, "PSEUDO")
                        else :agrandirbouton2(joinservc, creerservy, soloc, creerservu, nommulti)   
                        fenetre1.mainloop()
                else : caseentrable = 0
            elif y > validery and y < valideru:
                if x > solox and x< soloc:   
                    canvas = 3
                    caseentrable = 3
                    requetevaliderIPserveur()
                elif x > creerservx and x< creerservc:
                    print("ici")
                    canvas = 2
                    creercanvas()
                    loop = 0
                    multijoueur = 0
                else : caseentrable = 0
            else : caseentrable = 0
        elif canvas == 1:
            if y >= int(9.8*h/16) and y <= int(13*h/16):
                if len(competences[agent])/4 == 3:
                    if x >= int(8.4*l/16) and x <= int(10*l/16):
                        if demander1 > 0 :
                            demander1 -= 1
                        elif int(competences[agent][3])>0 :
                            competences[agent][3] = str(int(competences[agent][3])-1)
                    elif x >= int(10.2*l/16) and x <= int(11.8*l/16):
                        if demander2 > 0 :
                            demander2 -= 1
                        elif int(competences[agent][7])>0 :
                            competences[agent][7] = str(int(competences[agent][7])-1)
                    elif x >= int(12*l/16) and x <= int(13.6*l/16):
                        if demander3 > 0 :
                            demander3 -= 1
                        elif int(competences[agent][11])>0 :
                            competences[agent][11] = str(int(competences[agent][11])-1)
                elif len(competences[agent])/4 == 2:
                    if x >= int(9.2*l/16) and x <= int(10.8*l/16):
                        if demander1 > 0 :
                            demander1 -= 1
                        elif int(competences[agent][3])>0 :
                            competences[agent][3] = str(int(competences[agent][3])-1)
                    elif x >= int(11.2*l/16) and x <= int(12.8*l/16):
                        if demander2 > 0 :
                            demander2 -= 1
                        elif int(competences[agent][7])>0 :
                            competences[agent][7] = str(int(competences[agent][7])-1)
            elif y > retoury and y < retouru and x > retourx and x < retourc :
                canvas = 0
                round = 0

        agrandirimages(x,y)
        creercanvas()
    
def changerfond():
    if canvas == 1:
        fenetre1.configure(bg = couleursagents[agent])
    else:
        fenetre1.configure(bg = 'black')

def maj(event):
    global  l,h, fenetre1
    l = event.width
    h = event.height
    dimensionnertout()
    
    creercanvas()

def passagesouris(event):
    x = event.x
    y = event.y
    if activerclic:
        agrandirimages(x,y)

versionchercheur()
dimensionnertout()
creercanvas()

fenetre1.bind("<Motion>",passagesouris)
fenetre1.bind("<Button-1>",clic)
fenetre1.bind('<Configure>', maj)
fenetre1.bind_all("<Key>", touchepresee)

window.mainloop()