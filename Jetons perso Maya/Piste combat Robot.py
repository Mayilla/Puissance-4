# Code de la grille de jeu (Maya)
# + alternance jetons/joueurs 
# + sauvegarde/charger 

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
import json
import random


historique_coups = []

nom_J1 = "Jean"   #Juste pour tester pour l'intant à modif pour relier avec page inscription
nom_J2 = "Pierre"    


#https://docs.python.org/3/library/tkinter.html

# Taille de la grille de jeux
lignes = 6
colonnes = 7


# Couleurs utilisées : 
#Alors pour l'instant j'ai juste mis les couleur du jeux de base, a voir par la suite si on modifie

bleu = (0, 0, 255)  
rouge = (255, 0, 0)  
jaune = (255, 255, 0)
noir = (0,0,0)


# Création fenêtre
fenetre_grillejeux = tk.Tk()

#Prend taille écran en compte perso
ecran_largeur = fenetre_grillejeux.winfo_screenwidth() #https://sites.google.com/site/pythonpasapas/modules/tkinter/tkinter-methodes/tkinter-winfo_screenwidth
ecran_hauteur = fenetre_grillejeux.winfo_screenheight()

# donc ça devrait adapter 
taille_case = min(ecran_largeur // (colonnes + 2), ecran_hauteur // (lignes + 4))
rayon = int(taille_case / 2 - 5)


fenetre_grillejeux.geometry(f"{ecran_largeur}x{ecran_hauteur}") 
fenetre_grillejeux.title("Grille de jeux")
fenetre_grillejeux.state('zoomed')


# Compteur de victoires
victoires_joueur1 = 0
victoires_joueur2 = 0

manche = random.randint(0, 1)
cmpt = 0 
victoires_joueur2 = 0


# Label message gagnant dans le canvas
label_resultat = tk.Label(fenetre_grillejeux, text="Que le meilleur gagne ! 🎯", font=("Impact", 50))
label_resultat.pack(pady=(30, 0))

prochain_joueur = nom_J1 if (cmpt + manche) % 2 == 0 else nom_J2
couleur_texte = "red" if (cmpt + manche) % 2 == 0 else "#FFD700"
label_joueur = tk.Label(fenetre_grillejeux, text = f"{prochain_joueur} commence !", font=("Impact", 20), fg = couleur_texte)
label_joueur.pack()

#frames pour séparer canvas et boutons normalement aide si boutons apparaissent pas sur votre écran (normalement)
frame_canvas = tk.Frame(fenetre_grillejeux)
frame_canvas.pack()

frame_boutons = tk.Frame(fenetre_grillejeux)
frame_boutons.pack(pady=10)

canvas = tk.Canvas(frame_canvas, width=colonnes * taille_case, height=(lignes + 1) * taille_case)
canvas.pack()


# Création grille de base donc vide
def creation_grille():
    grille = np.zeros((lignes, colonnes))  #soit matrice 6x7
    return grille

grille = creation_grille() 



#Afficher messages quand réalise action boutons (à voir et rendre plus propre)
message_label = tk.Label(fenetre_grillejeux, text="", font=("Arial", 14), fg="green")
message_label.pack(pady=10)



# Fonction pour tracer grille et emplacements jetons
def tracer_grille(grille):
    canvas.delete("all") 
    # Base de la grille
    for i in range(colonnes):
        for j in range(lignes):
            canvas.create_rectangle(i*taille_case, j*taille_case + taille_case, (i + 1)*taille_case, (j + 1)*taille_case + taille_case, fill="blue", outline="black")
            canvas.create_oval(i*taille_case + 10, j*taille_case + taille_case + 10, (i + 1)*taille_case - 10, (j + 1)*taille_case + taille_case - 10, fill="black")
    # Places jetons
    for i in range(colonnes):
        for j in range(lignes):
            if grille[j][i] == 1:  # pour quand alterne J1
                canvas.create_oval(i*taille_case + 10, (lignes -j - 1)*taille_case + taille_case + 10, (i + 1)*taille_case - 10, (lignes -j)*taille_case + taille_case - 10, fill="red")
            elif grille[j][i] == 2:  # pour quand alterne J2
                canvas.create_oval(i* taille_case + 10, (lignes -j - 1)*taille_case + taille_case + 10, (i + 1)*taille_case - 10, (lignes-j)*taille_case + taille_case - 10, fill="yellow")

#décalage pour l'instant en fonction de la taille grille mais a rendre modifiable

# Alors j'ai pensé un peu au placement des jetons par clic, c'est pas encore ça + faut alterner les joueurs mieux mais l'idée est là
# doc thinker event : https://docs.python.org/3/library/tkinter.html#bindings-and-events


# Kinga : J'ai modifié cette fonction comme ca si y a une colonne remplie il se passe rien qd on appuie
#Maya : j'ai modifier pour pas erreur avec le robot
def ajouter_jeton(grille, col, J):
    for i in range(lignes):
        if grille[i][col] == 0:
            grille[i][col] = J
            return
    return None  #col pleine



def est_un_coup_gagnant(grille, col, joueur): #pour faire comprendre au robot
    """Retourne True si l'action du joueur va le faire gagner"""

    for i in range(lignes):
        if grille[i][col] == 0:
            ligne = i
            break
    else:
        return False  #déjà plein

    grille[ligne][col] = joueur

    gagnant = check_gagnant(grille)

    grille[ligne][col] = 0 #reset coup

    return gagnant == joueur



def clic_canvas(event):
    global grille, cmpt
    if (cmpt + manche) % 2 == 0:  #humain
        grille, cmpt = alternance_joueur(event, grille, taille_case, colonnes, cmpt)
        gagnant = check_gagnant(grille) #là il vérif si il y a un coup gagant possible
        if gagnant != 0:
            couleur = "Rouge" if gagnant == 1 else "Jaune"
            if gagnant == 1:
                global victoires_joueur1
                victoires_joueur1 += 1
                label_resultat.config(text=f"{nom_J1} a gagné ! 🎉", fg="red")
            else:
                global victoires_joueur2
                victoires_joueur2 += 1
                label_resultat.config(text=f"{nom_J2} a gagné ! 🎉", fg="#FFD700")
            
            canvas.unbind("<Button-1>") #on peut plus cliquer
            label_joueur.config(text="")
        elif np.all(grille != 0):
            label_resultat.config(text="Match nul ! 😅", fg="black")
            canvas.unbind("<Button-1>")
        else:
            fenetre_grillejeux.after(500, jouer_contre_robot) #obliger délai sinon on voit meme pas le coup



def jouer_contre_robot():
    global grille, cmpt

    colonnes_valides = [col for col in range(colonnes) if grille[lignes - 1][col] == 0]
    if not colonnes_valides:
        return

    #robot veut gagner
    for col in colonnes_valides:
        if est_un_coup_gagnant(grille, col, 2): #2 c'est robot
            ajouter_jeton(grille, col, 2)
            tracer_grille(grille)
            cmpt += 1
            historique_coups.append(col)
            return

    #robot veut bloquer J
    for col in colonnes_valides:
        if est_un_coup_gagnant(grille, col, 1): 
            ajouter_jeton(grille, col, 2)
            tracer_grille(grille)
            cmpt += 1
            historique_coups.append(col)
            return

    #robot coup aléatoire
    col_choisie = random.choice(colonnes_valides)
    ajouter_jeton(grille, col_choisie, 2)
    tracer_grille(grille)
    cmpt += 1
    historique_coups.append(col_choisie)




def alternance_joueur(event, grille, taille_case, colonnes, cmpt):
    if (cmpt + manche) % 2 == 0:  #humain
        J = 1 
        colonne_clique = event.x // taille_case
        if colonne_clique >= colonnes:
            return grille, cmpt
        ajouter_jeton(grille, colonne_clique, J)
    else: 
        J = 2  #robot
        fenetre_grillejeux.after(500, jouer_contre_robot)


    tracer_grille(grille)
    cmpt += 1
    return grille, cmpt

####

cmpt = 0

canvas.bind("<Button-1>", clic_canvas)

tracer_grille(grille)

#Remettre a zero la grille à chaque ouverture de la fenetre :

def reset_grille():
    global grille, cmpt, historique_coups, manche
    manche += 1
    grille = creation_grille()  
    cmpt = 0  #reset tout
    historique_coups.clear()
    tracer_grille(grille)
    message_label.config(text="Grille bien réinitialisée", fg="orange")
    fenetre_grillejeux.after(3000, lambda: message_label.config(text="")) #mis pour 3s
    canvas.bind("<Button-1>", clic_canvas)
    label_resultat.config(                      
        text=f"{nom_J1} - {victoires_joueur1}  ||  {nom_J2} - {victoires_joueur2}",
        fg="black"
    )
    prochain_joueur = nom_J1 if (cmpt + manche) % 2 == 0 else nom_J2
    couleur_texte = "red" if prochain_joueur == "Rouge" else "#FFD700"
    label_joueur.config(text=f"{prochain_joueur} commence !", fg=couleur_texte)

    #donc la robot va jouer
    if (cmpt + manche) % 2 != 0:
        fenetre_grillejeux.after(500, jouer_contre_robot)  # Plus rapide pour éviter un trop long délai



#fonction sauvegarder/charger pour l'instant

def sauvegarder_partie():
    nom_fichier = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichier JSON", "*.json")]) #comme ça on écrit ce qu'on veut comme nom
    if not nom_fichier:
        return
    donnees = {
        "grille": grille.tolist(),
        "tour": cmpt,
        "historique": historique_coups
    }
    with open(nom_fichier, "w") as fichier:
        json.dump(donnees, fichier)
    message_label.config(text=f"Partie sauvegardée sous {nom_fichier}", fg="green")
    fenetre_grillejeux.after(3000, lambda: message_label.config(text=""))


def charger_partie():
    global grille, cmpt, historique_coups
    nom_fichier = filedialog.askopenfilename(defaultextension=".json", filetypes=[("Fichier JSON", "*.json")])
    if not nom_fichier:
        return
    with open(nom_fichier, "r") as fichier:
        donnees = json.load(fichier)
    grille = np.array(donnees["grille"])
    cmpt = donnees["tour"]
    historique_coups = donnees["historique"]
    tracer_grille(grille)
    message_label.config(text=f"Partie chargée à partir de {nom_fichier}", fg="blue")
    fenetre_grillejeux.after(3000, lambda: message_label.config(text=""))

def nouvelle_partie():
    global grille, cmpt, victoires_joueur1, victoires_joueur2, manche
    manche = random.randint(0, 1)
    grille = creation_grille()
    cmpt = 0
    victoires_joueur1 = 0
    victoires_joueur2 = 0
    tracer_grille(grille)
    canvas.bind("<Button-1>", clic_canvas)
    label_resultat.config(text="Que le meilleur gagne ! 🎯", fg="black")
    label_resultat.config(text=f"{nom_J1} - {victoires_joueur1}  ||  {nom_J2} - {victoires_joueur2}", fg="black")
    prochain_joueur = nom_J1 if (cmpt + manche) % 2 == 0 else nom_J2
    couleur_texte = "red" if (cmpt + manche) % 2 == 0 else "#FFD700"
    label_joueur.config(text = f"{prochain_joueur} commence !", fg = couleur_texte)

def check_gagnant(grille):
    lignes, colonnes = grille.shape

    for ligne in range(lignes):
        for col in range(colonnes):
            joueur = grille[ligne][col]
            if joueur == 0:
                continue

            # Horizontal
            if col + 3 < colonnes and all(grille[ligne][col + i] == joueur for i in range(4)):
                return joueur

            # Vertical
            if ligne + 3 < lignes and all(grille[ligne + i][col] == joueur for i in range(4)):
                return joueur

            # Diagonale descendante
            if ligne + 3 < lignes and col + 3 < colonnes and all(grille[ligne + i][col + i] == joueur for i in range(4)):
                return joueur

            # Diagonale montante
            if ligne - 3 >= 0 and col + 3 < colonnes and all(grille[ligne - i][col + i] == joueur for i in range(4)):
                return joueur

    return 0  # pas de gagnant


#Tous les bontons a afficher : 
bouton_reset = tk.Button(frame_boutons, text="Nettoyer la grille", command=reset_grille)
bouton_reset.pack(side=tk.LEFT, padx=10)

bouton_nvl_partie = tk.Button(frame_boutons, text = "Recommencer", command = nouvelle_partie)
bouton_nvl_partie.pack(side=tk.LEFT, padx=10)

bouton_sauvegarder = tk.Button(frame_boutons, text="Sauvegarder", command=sauvegarder_partie)
bouton_sauvegarder.pack(side=tk.LEFT, padx=10)

bouton_charger = tk.Button(frame_boutons, text="Charger", command=charger_partie)
bouton_charger.pack(side=tk.LEFT, padx=10)


fenetre_grillejeux.mainloop()