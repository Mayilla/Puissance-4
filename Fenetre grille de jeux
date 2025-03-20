#biblio nécessaire
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

#https://docs.python.org/3/library/tkinter.html

# Taille de la grille de jeux
lignes = 6
colonnes = 7
taille_case = 100
rayon = int(taille_case /2-5)

# Couleurs utilisées : 
#Alors pour l'instant j'ai juste mis les couleur du jeux de base, a voir par la suite si on modifie

bleu = (0, 0, 255)  
rouge = (255, 0, 0)  
jaune = (255, 255, 0)
noir = (0,0,0)


# Création fenêtre
fenetre_grillejeux = tk.Tk()
fenetre_grillejeux.geometry("1300x700")
fenetre_grillejeux.title("Grille de jeux")
fenetre_grillejeux.state('zoomed')

# Création du canvas
canvas = tk.Canvas(fenetre_grillejeux, width=colonnes * taille_case, height=(lignes + 1) * taille_case)
canvas.pack()

# Création grille de base donc vide
def creation_grille():
    grille = np.zeros((lignes, colonnes))  #soit matrice 6x7
    return grille

grille = creation_grille() 

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


# Initialisation de la grille et dessin initial
tracer_grille(grille)

# Démarrer la boucle principale de Tkinter
fenetre_grillejeux.mainloop()
