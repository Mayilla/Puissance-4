# Code - page accueil + nbr joueur + jeu + paramètres

# Bibliothèques nécessaires
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
import json

###########################################################################################################################################
###########################################################################################################################################
# Code page des règles / Rehan

def f_fenetre_regle() :

    # Création fenêtre règles
    fenetre_regles = tk.Toplevel()
    fenetre_regles.title("Règles")
    fenetre_regles.geometry("1300x700")
    fenetre_regles.state("zoomed")
    fenetre_regles.configure(bg = '#ffd88e')


    # Callbacks
    def retour_menu() :
        fenetre_regles.destroy()


    # Contenu fenêtre règles
    text_annonce_regle = tk.Label(fenetre_regles, text = "Voici les règles de notre jeu, veuillez les respecter.", font=("Comic Sans MS", 23, "bold"), bg = '#ffecaf', fg="#a97c11")
    text_annonce_regle.place(relx=0.5, rely=0.1, anchor="center")

    text_regle1 = tk.Label(fenetre_regles, text = "Puissance X est un jeu de stratégie pour deux joueurs où l'objectif est d'aligner X jetons de sa couleur dans une grille.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle1.place(relx=0.5, rely=0.2, anchor="center")

    text_regle2 = tk.Label(fenetre_regles, text = "Règles principales :", bg = '#ffecaf', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle2.place(relx=0.5, rely=0.3, anchor="center")

    text_regle3 = tk.Label(fenetre_regles, text = "But du jeu : Chaque joueur doit former un alignement de X jetons de sa couleur. L'alignement peut être horizontal, vertical ou diagonal.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle3.place(relx=0.5, rely=0.35, anchor="center")

    text_regle4 = tk.Label(fenetre_regles, text = "La grille : La grille comporte 6, 7 ou 8 colonnes et 5, 6 ou 7 rangées. Les jetons tombent dans la colonne choisie et s'empilent.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle4.place(relx=0.5, rely=0.4, anchor="center")

    text_regle5 = tk.Label(fenetre_regles, text = "Déroulement :", bg = '#ffecaf', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle5.place(relx=0.5, rely=0.5, anchor="center")

    text_regle6 = tk.Label(fenetre_regles, text = "Les joueurs jouent à tour de rôle. A chaque tour, un joueur place un jeton dans une colonne.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle6.place(relx=0.5, rely=0.55, anchor="center")

    text_regle7 = tk.Label(fenetre_regles, text = "Victoire : La partie se termine lorsqu’un joueur réussit à aligner X jetons, ou si la grille est entièrement remplie sans gagnant, c'est-à-dire match nul.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle7.place(relx=0.5, rely=0.6, anchor="center")

    text_regle8 = tk.Label(fenetre_regles, text = "C'est un jeu qui mélange chance et stratégie, parfait pour tester vos réflexes et votre sens de la stratégie.", bg = '#ffd88e', fg="#a97c11", font=("Comic Sans MS", 12, "bold"))
    text_regle8.place(relx=0.5, rely=0.65, anchor="center")

    Bouton_retour_menu = tk.Button(fenetre_regles, text = "Retourner au menu principal", font=("Comic Sans MS", 10, "bold"), fg = '#ffd88e', bg="#a97c11", command= retour_menu)
    Bouton_retour_menu.place(relx=0.5, rely=0.8, anchor="center")
    
    bouton_quitter = tk.Button(fenetre_regles, text = "X", bg = "red", fg = "white", font = ("Helvetica", 10, "bold"), command = retour_menu)
    bouton_quitter.place(relx = 1.0, x = -3, y = 2.5, anchor = "ne")

    #On affiche la fenetre :
    fenetre_regles.mainloop()


###########################################################################################################################################
###########################################################################################################################################
# Code de la fenêtre du choix de joueurs / Loïs
# Code - page accueil + nbr joueur + jeu + paramètres

# Bibliothèques nécessaires
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
import json

# Variables globales
joueur_1 = 'humain'
joueur_2 = 'humain'
texte_joueur_1 = "-"
texte_joueur_2 = "-"


def f_fenetre_nombre_joueur():
    global joueur_1, joueur_2, texte_joueur_1, texte_joueur_2

    # Création de la fenêtre
    fenetre_nom_joueur = tk.Toplevel()
    fenetre_nom_joueur.geometry("1300x700")
    fenetre_nom_joueur.title("Nombre de joueurs")
    fenetre_nom_joueur.state('zoomed') # Plein écran
    fenetre_nom_joueur.configure(bg='#ffd88e')

    # Charger les images
    image1 = ImageTk.PhotoImage(Image.open("Image joueur humain.png"))
    image2 = ImageTk.PhotoImage(Image.open("Image joueur 2 humain.png"))
    image3 = ImageTk.PhotoImage(Image.open("Image joueur robot.png"))


    # Fonctions de commande
        # Fonction fermer la fenêtre (deviendra après un retour à la fenêtre précédente)
    def quitter():
        fenetre_nom_joueur.destroy()


        # Fonction pour vérifier si noms validés
    def valider_noms():
        if texte_joueur_1 == "-" or texte_joueur_2 == "-":
            print("Veuillez entrer les noms des joueurs.")
            return False
        return True


        # Fonction lancer la partie (relie la page de jeu)
    message_label = tk.Label(fenetre_nom_joueur, text="", font=("Arial", 14), fg="green", bg = "#ffd88e")
    message_label.place(relx=0.5, y=590, anchor = "center")

    def lancer_partie():
        # Si noms pas validés
        if valider_noms() == False:
            message_label.config(text="Veuillez entrer les noms des joueurs", font=("Comic Sans MS", 12, "bold"), fg = "#a97c11", bg = "#ffd88e")
            return
        print("Lancer la partie !")
        fenetre_nom_joueur.destroy()
        f_fenetre_grille_jeux()


        # Fonction affichage noms des joueurs
    def mettre_a_jour_label_noms():
        text_nom_joueurs.config(text = f"Joueur 1 : {texte_joueur_1} \n Joueur 2 : {texte_joueur_2}")


        # Fonction pour enregistrer le texte saisi sous le bouton 1
    def enregistrer_texte_1():
        global texte_joueur_1
        texte_joueur_1 = champ_texte_1.get()
        print(f"Texte enregistré pour le bouton 1 : {texte_joueur_1}")
        mettre_a_jour_label_noms()


        # Fonction pour enregistrer le texte saisi sous le bouton 2
    def enregistrer_texte_2():
        global texte_joueur_2
        texte_joueur_2 = champ_texte_2.get()
        print(f"Texte enregistré pour le bouton 2 : {texte_joueur_2}")
        mettre_a_jour_label_noms()


        # Fonction pour changer l'image du bouton joueur 1
    def changer_image():
        global joueur_1, joueur_2, texte_joueur_1

        if joueur_1 == "humain":
            if joueur_2 == "robot":
                print("Impossible : déjà un robot en joueur 2.")
                return
            joueur_1 = "robot"
            texte_joueur_1 = "Robot"
            bouton_1.config(image=image3)
            champ_texte_1.delete(0, "end")
            champ_texte_1.insert(0, "Robot")
            champ_texte_1.config(state="disabled")
        else:
            joueur_1 = "humain"
            texte_joueur_1 = "-"
            bouton_1.config(image=image1)
            champ_texte_1.config(state="normal")
            champ_texte_1.delete(0, "end")
            champ_texte_1.insert(0, "Nom joueur 1")

        mettre_a_jour_label_noms()



        # Fonction pour changer l'image du bouton joueur 2
    def changer_image_2():
        global joueur_1, joueur_2, texte_joueur_2

        if joueur_2 == "humain":
            if joueur_1 == "robot":
                print("Impossible : déjà un robot en joueur 1.")
                return
            joueur_2 = "robot"
            texte_joueur_2 = "Robot"
            bouton_2.config(image=image3)
            champ_texte_2.delete(0, "end")
            champ_texte_2.insert(0, "Robot")
            champ_texte_2.config(state="disabled")
        else:
            joueur_2 = "humain"
            texte_joueur_2 = "-"
            bouton_2.config(image=image2)
            champ_texte_2.config(state="normal")
            champ_texte_2.delete(0, "end")
            champ_texte_2.insert(0, "Nom joueur 2")

        mettre_a_jour_label_noms()



            # Fonction pour ajouter une indication dans un champ de saisie
    def ajouter_indication(champ, texte):
        champ.insert(0, texte)
        champ.bind("<FocusIn>", lambda event: supprimer_indication(champ, texte))
        champ.bind("<FocusOut>", lambda event: restaurer_indication(champ, texte))


        # Fonction pour supprimer l'indication lorsque l'utilisateur clique dans le champ
    def supprimer_indication(champ, texte):
        if champ.get() == texte:
            champ.delete(0, "end")


        # Fonction pour restaurer le indication si le champ est vide
    def restaurer_indication(champ, texte):
        if champ.get() == "":
            champ.insert(0, texte)



    # Contenu fenêtre des paramètres
    text_principal = tk.Label(fenetre_nom_joueur, text = "Nombre de joueurs", font = ("Comic Sans MS", 23, "bold"), bg = "#ffecaf", fg = "#a97c11")
    text_principal.place(relx=0.5, y=80, anchor = "center")

    text_consignes = tk.Label(fenetre_nom_joueur, text = "Vous pouvez choisir vos noms de joueurs ainsi que le mode de jeu : 2 joueurs ou contre l'IA. \n Pour cela, cliquez sur les images.", font = ("Comic Sans MS", 18), bg = "#ffd88e", fg = "#a97c11")
    text_consignes.place(relx=0.5, y=151, anchor = "center")

    text_nom_joueurs = tk.Label(fenetre_nom_joueur, text = f"Joueur 1 : {texte_joueur_1} \n Joueur 2 : {texte_joueur_2}", font = ("Comic Sans MS", 18), bg = "#ffd88e", fg = "#a97c11")
    text_nom_joueurs.place(relx=0.5, y=455, anchor = "center")


        # Boutons pour choisir le type de joueur
    bouton_1 = tk.Button(fenetre_nom_joueur, text = "", width = 100, height = 100, image=image1, bd = 0, highlightthickness = 0, bg = '#ffd88e', compound = "center", command = changer_image)
    bouton_1.place(relx=0.4, rely=0.4, anchor = "center")

    bouton_2 = tk.Button(fenetre_nom_joueur, text = "", width = 100, height = 100, image=image2, bd = 0, highlightthickness = 0, bg = '#ffd88e', compound = "center", command = changer_image_2)
    bouton_2.place(relx=0.6, rely=0.4, anchor = "center")


        # Boutons pour enregistrer le texte
    bouton_enregistrer_1 = tk.Button(fenetre_nom_joueur, text = "Enregistrer", font =("Helvetica", 10), bg = "#a97c11", fg = "#ffecaf", command = enregistrer_texte_1)
    bouton_enregistrer_1.place(relx=0.4, rely=0.59, anchor = "center")

    bouton_enregistrer_2 = tk.Button(fenetre_nom_joueur, text = "Enregistrer", font = ("Helvetica", 10), bg = "#a97c11", fg = "#ffecaf", command = enregistrer_texte_2)
    bouton_enregistrer_2.place(relx=0.6, rely=0.59, anchor = "center")


        # Champs de saisie pour entrer du texte avec placeholders
    champ_texte_1 = tk.Entry(fenetre_nom_joueur, width = 20, font = ("Helvetica", 12), fg = "grey", bg = "#ffecaf")
    champ_texte_1.place(relx=0.4, rely=0.53, anchor = "center")
    ajouter_indication(champ_texte_1, "Nom joueur 1")

    champ_texte_2 = tk.Entry(fenetre_nom_joueur, width = 20, font = ("Helvetica", 12), fg = "grey", bg = "#ffecaf")
    champ_texte_2.place(relx=0.6, rely=0.53, anchor = "center")
    ajouter_indication(champ_texte_2, "Nom joueur 2")


        # Bouton permettant de quitter la fenêtre (et de revenir à la fenêtre précédente dans un futur lointain)
    bouton_quitter = tk.Button(fenetre_nom_joueur, text = "⤶", bg = 'red', fg = "white", font = ("Comic Sans MS", 10, "bold"), command = quitter)
    bouton_quitter.place(relx = 1.0, x=-3, y=2.5, anchor = "ne")


        # Bouton pour lancer la partie
    bouton_lancer_partie = tk.Button(fenetre_nom_joueur, text = "Lancer la partie", font = ("Comic Sans MS", 18, "bold"), bg = "#ffecaf", fg = "#a97c11", command = lancer_partie)
    bouton_lancer_partie.place(relx=0.5, y=545, anchor = "center")


    # On affiche la fenêtre
    fenetre_nom_joueur.mainloop()



###########################################################################################################################################
###########################################################################################################################################



###########################################################################################################################################
###########################################################################################################################################
# Code de la fenêtre des paramètres

def f_fenetre_parametres():
    # Création de la fenêtre des paramètres	
    fenetre_parametres = tk.Toplevel()
    fenetre_parametres.geometry("1300x700")
    fenetre_parametres.title("Paramètres")
    fenetre_parametres.state('zoomed')
    fenetre_parametres.configure(bg='#ffd88e')


    # Fonctions de commande

        # Fonction fermer la fenêtre (deviendra après un retour à la fenêtre précédente)
    def quitter():
        fenetre_parametres.destroy()

        # Fonction boutons choix thème grille
    def choix_grille(theme_g):
        global theme_grille_selectionne
        theme_grille_selectionne = theme_g
        print(f"Thème sélectionné : {theme_grille_selectionne}")

        # Fonction boutons choix thème jetons
    def choix_jetons(theme_j):
        global theme_jetons_selectionne
        theme_jetons_selectionne = theme_j
        print(f"Thème sélectionné : {theme_jetons_selectionne}")

        # Fonction boutons choix taille grille
    def choix_taille(taille_g):
        global taille_selectionnee
        taille_selectionnee = taille_g
        print(f"Taille sélectionnée : {taille_selectionnee}")



    # Contenu fenêtre des paramètres
    text_principal = tk.Label(fenetre_parametres, text = "Paramètres", font=("Comic Sans MS", 23, "bold"), bg="#ffecaf", fg="#a97c11")
    text_principal.place(relx=0.5, y=70, anchor="center")

        # Texte pour le choix de la grille
    text_grille = tk.Label(fenetre_parametres, text = "Thème de la grille :", font=("Comic Sans MS", 15, "bold"), bg="#ffecaf", fg="#a97c11")
    text_grille.place(x = 70, y = 125)

            # Boutons pour le choix de la grille
    grille_bleue = Image.open("C:/Users/loisc/OneDrive/Bureau/Université/1ère année/Semestre 2/Informatique - bases de Python/Puissance_4/Thème bleu grille.png")
    grille_bleue = ImageTk.PhotoImage(grille_bleue)
    bouton_grille1 = tk.Button(fenetre_parametres, text = "", width=110, height=70, image=grille_bleue, compound="center", command = lambda: choix_grille("bleu"))
    bouton_grille1.place(x = 180, y = 170)

    grille_bois = Image.open("Thème bois grille.png")
    grille_bois = ImageTk.PhotoImage(grille_bois)
    bouton_grille2 = tk.Button(fenetre_parametres, text = "", width = 110, height = 70, image = grille_bois, compound = "center", command = lambda: choix_grille("bois"))
    bouton_grille2.place(x = 380, y = 170)

    grille_enfants = Image.open("Thème enfants grille.png")
    grille_enfants = ImageTk.PhotoImage(grille_enfants)
    bouton_grille3 = tk.Button(fenetre_parametres, text = "", width = 110, height = 70, image = grille_enfants, compound = "center", command = lambda: choix_grille("enfants"))
    bouton_grille3.place(x = 580, y = 170)

    grille_nature = Image.open("Thème nature grille.png")
    grille_nature = ImageTk.PhotoImage(grille_nature)
    bouton_grille4 = tk.Button(fenetre_parametres, text = "", width = 110, height = 70, image = grille_nature, compound = "center", command = lambda: choix_grille("nature"))
    bouton_grille4.place(x = 780, y = 170)

    grille_game = Image.open("Thème game grille.png")
    grille_game = ImageTk.PhotoImage(grille_game)
    bouton_grille5 = tk.Button(fenetre_parametres, text = "", width = 110, height = 70, image = grille_game, compound = "center", command = lambda: choix_grille("game"))
    bouton_grille5.place(x = 980, y = 170)

        # Texte pour le choix des jetons
    text_jetons = tk.Label(fenetre_parametres, text = "Thème des jetons :", font=("Comic Sans MS", 15, "bold"), bg="#ffecaf", fg="#a97c11")
    text_jetons.place(x = 70, y = 275)

            # Bouttons pour le choix des jetons
    jetons_r_j = Image.open("Thème rouge-jaune jetons.png")
    jetons_r_j = ImageTk.PhotoImage(jetons_r_j)
    bouton_jetons2 = tk.Button(fenetre_parametres, text = "", width = 100, height = 100, image = jetons_r_j, compound = "center", bd = 0, highlightthickness = 0, bg = '#ffd88e', command = lambda: choix_jetons("rouge-jaune"))
    bouton_jetons2.place(x = 190, y = 320)

    jetons_chien_chat = Image.open("Thème chien-chat jetons.png")
    jetons_chien_chat = ImageTk.PhotoImage(jetons_chien_chat)
    bouton_jetons3 = tk.Button(fenetre_parametres, text = "", width = 100, height = 100, image = jetons_chien_chat, compound = "center", bd = 0, highlightthickness = 0, bg = '#ffd88e', command = lambda: choix_jetons("chien-chat"))
    bouton_jetons3.place(x = 390, y = 320)


    jetons_nous = Image.open("Double jetons perso.png")
    jetons_nous = ImageTk.PhotoImage(jetons_nous)
    bouton_jetons3 = tk.Button(fenetre_parametres, text = "", width = 100, height = 100, image = jetons_nous, compound = "center", bd = 0, highlightthickness = 0, bg = '#ffd88e', command = lambda: choix_jetons("nous"))
    bouton_jetons3.place(x = 590, y = 320)


    jetons_fleurs = Image.open("Thème fleurs jetons.png")
    jetons_fleurs = ImageTk.PhotoImage(jetons_fleurs)
    bouton_jetons2 = tk.Button(fenetre_parametres, text = "", width = 100, height = 100, image = jetons_fleurs, compound = "center", bd = 0, highlightthickness = 0, bg = '#ffd88e', command = lambda: choix_jetons("fleurs"))
    bouton_jetons2.place(x = 790, y = 320)

    jetons_robot = Image.open("Thème robot jetons.png")
    jetons_robot = ImageTk.PhotoImage(jetons_robot)
    bouton_jetons3 = tk.Button(fenetre_parametres, text = "", width = 100, height = 100, image = jetons_robot, compound = "center", bd = 0, highlightthickness = 0, bg = '#ffd88e', command = lambda: choix_jetons("robot"))
    bouton_jetons3.place(x = 990, y = 320)

        # Texte pour le choix de la taille de grille
    text_taille = tk.Label(fenetre_parametres, text = "Taille du jeu :", font=("Comic Sans MS", 15, "bold"), bg="#ffecaf", fg="#a97c11")
    text_taille.place(x = 70, y = 450)

            # Boutons pour le choix de la taille de grille
    bouton_taille1 = tk.Button(fenetre_parametres, text = "Puissance 3\n6x5", font=("Comic Sans MS", 12, "bold"), bg = "#a97c11", fg = "#ffd88e", width = 9, height = 2, command = lambda: choix_taille("3"))
    bouton_taille1.place(x = 290, y = 490)

    bouton_taille2 = tk.Button(fenetre_parametres, text = "Puissance 4\n7x6", font=("Comic Sans MS", 12, "bold"), bg = "#a97c11", fg = "#ffd88e", width = 9, height = 2, command = lambda: choix_taille("4"))
    bouton_taille2.place(x = 590, y = 490)

    bouton_taille3 = tk.Button(fenetre_parametres, text = "Puissance 5\n8x7", font=("Comic Sans MS", 12, "bold"), bg = "#a97c11", fg = "#ffd88e", width = 9, height = 2, command = lambda: choix_taille("5"))
    bouton_taille3.place(x = 890, y = 490)


    # Bouton permettant de quitter la fenêtre (et de revenir à la fenêtre précédente dans un futur lointain)
    bouton_quitter = tk.Button(fenetre_parametres, text = "X", bg = "red", fg = "white", font = ("Helvetica", 10, "bold"), command = quitter)
    bouton_quitter.place(relx = 1.0, x = -3, y = 2.5, anchor = "ne")


    # On affiche la fenêtre
    fenetre_parametres.mainloop()


###########################################################################################################################################
###########################################################################################################################################
# Code de la grille de jeu (Maya)
# + alternance jetons/joueurs 
# + sauvegarde/charger 

historique_coups = []

#https://docs.python.org/3/library/tkinter.html

# Taille de la grille de jeux
lignes = 6
colonnes = 7
taille_case = 70
rayon = int(taille_case /2-5)


# Couleurs utilisées : 
#Alors pour l'instant j'ai juste mis les couleur du jeux de base, a voir par la suite si on modifie

bleu = (0, 0, 255)  
rouge = (255, 0, 0)  
jaune = (255, 255, 0)
noir = (0,0,0)

def f_fenetre_grille_jeux():
    global grille_theme_selectionne, theme_jetons_selectionne, taille_selectionnee, lignes, colonnes, taille_case, jeton_joueur_1, jeton_joueur_2, grille_theme

    # Récupérer les thèmes et la taille sélectionnés
    if 'theme_grille_selectionne' in globals():
        grille_theme_selectionne = theme_grille_selectionne
    else:
        grille_theme_selectionne = "bleu"  # Valeur par défaut

    if 'theme_jetons_selectionne' in globals():
        theme_jetons_selectionne = theme_jetons_selectionne
    else:
        theme_jetons_selectionne = "rouge-jaune"  # Valeur par défaut

    if 'taille_selectionnee' in globals():
        taille_selectionnee = taille_selectionnee
    else:
        taille_selectionnee = "4"  # Valeur par défaut


    # Ajuster la taille de la grille en fonction de la sélection
    if taille_selectionnee == "3":
        lignes = 5
        colonnes = 6
        taille_case = 70
    elif taille_selectionnee == "4":
        lignes = 6
        colonnes = 7
        taille_case = 70
    elif taille_selectionnee == "5":
        lignes = 7
        colonnes = 8
        taille_case = 70


    # Création fenêtre
    fenetre_grillejeux = tk.Toplevel()
    fenetre_grillejeux.geometry("800x500")
    fenetre_grillejeux.title("Grille de jeux")
    fenetre_grillejeux.state('zoomed')
    # Fond de la fenêtre
        # Charger l'image de fond
    fond_image = Image.open("Image fond jaune.png")
    fond_photo = ImageTk.PhotoImage(fond_image)

        # Créer le label pour l'image de fond

    label_fond = tk.Label(fenetre_grillejeux, image=fond_photo)
    label_fond.place(x=0, y=0, relwidth=1, relheight=1)


    # Choix des jetons selon la sélection
    if theme_jetons_selectionne == "rouge-jaune":
        jeton_joueur_1 = Image.open("Thème jaune jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_1 = ImageTk.PhotoImage(jeton_joueur_1)
        jeton_joueur_2 = Image.open("Thème rouge jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_2 = ImageTk.PhotoImage(jeton_joueur_2)
    elif theme_jetons_selectionne == "chien-chat":
        jeton_joueur_1 = Image.open("Thème chat jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_1 = ImageTk.PhotoImage(jeton_joueur_1)
        jeton_joueur_2 = Image.open("Thème chien jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_2 = ImageTk.PhotoImage(jeton_joueur_2)
    elif theme_jetons_selectionne == "fleurs":
        jeton_joueur_1 = Image.open("Thème fleur rose jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_1 = ImageTk.PhotoImage(jeton_joueur_1)
        jeton_joueur_2 = Image.open("Thème fleur blanche jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_2 = ImageTk.PhotoImage(jeton_joueur_2)
    elif theme_jetons_selectionne == "nous":
        jeton_joueur_1 = Image.open("Jeton perso Kinga-Rehan.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_1 = ImageTk.PhotoImage(jeton_joueur_1)
        jeton_joueur_2 = Image.open("Jeton perso Loïs-Maya.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_2 = ImageTk.PhotoImage(jeton_joueur_2)
    elif theme_jetons_selectionne == "robot":
        jeton_joueur_1 = Image.open("Thème robot jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_1 = ImageTk.PhotoImage(jeton_joueur_1)
        jeton_joueur_2 = Image.open("Thème robot jetons.png").resize((taille_case - 19, taille_case - 19))
        jeton_joueur_2 = ImageTk.PhotoImage(jeton_joueur_2)


    # Choix du thème de la grille selon la sélection
    if grille_theme_selectionne == "bleu":
        grille_theme = Image.open("Thème bleu grille.png").resize((colonnes*taille_case, (lignes + 1)*taille_case), Image.Resampling.LANCZOS)
        grille_theme = ImageTk.PhotoImage(grille_theme)
    elif grille_theme_selectionne == "bois":
        grille_theme = Image.open("Thème bois grille.png").resize((colonnes*taille_case, (lignes + 1)*taille_case), Image.Resampling.LANCZOS)
        grille_theme = ImageTk.PhotoImage(grille_theme)
    elif grille_theme_selectionne == "enfants":
        grille_theme = Image.open("Thème enfants grille.png").resize((colonnes*taille_case, (lignes + 1)*taille_case), Image.Resampling.LANCZOS)
        grille_theme = ImageTk.PhotoImage(grille_theme)
    elif grille_theme_selectionne == "nature":
        grille_theme = Image.open("Thème nature grille.png").resize((colonnes*taille_case, (lignes + 1)*taille_case), Image.Resampling.LANCZOS)
        grille_theme = ImageTk.PhotoImage(grille_theme)
    elif grille_theme_selectionne == "game":
        grille_theme = Image.open("Thème game grille.png").resize((colonnes*taille_case, (lignes + 1)*taille_case), Image.Resampling.LANCZOS)
        grille_theme = ImageTk.PhotoImage(grille_theme)


    # Ajouter un espace vide au-dessus du canvas
    frame_espace = tk.Frame(fenetre_grillejeux, height=50, bg="#ffd88e")  # Ajustez la hauteur (50) selon vos besoins
    frame_espace.pack(fill=tk.X)

    #frames pour séparer canvas et boutons normalement aide si boutons apparaissent pas sur votre écran (normalement)
    frame_canvas = tk.Frame(fenetre_grillejeux)
    frame_canvas.pack()

    frame_boutons = tk.Frame(fenetre_grillejeux, bg="#ffd88e")
    frame_boutons.pack(pady=10)


    #Canvas simple
    canvas = tk.Canvas(frame_canvas, width=colonnes * taille_case, height=lignes * taille_case)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=grille_theme)


    # Création grille de base donc vide
    def creation_grille():
        grille = np.zeros((lignes, colonnes))  #soit matrice 6x7
        return grille

    grille = creation_grille() 



    #Afficher messages quand réalise action boutons (à voir et rendre plus propre)
    message_label = tk.Label(fenetre_grillejeux, text="", font=("Arial", 14), fg="green")
    message_label.pack(pady=10)


    def tracer_grille(grille):
        canvas.delete("all") 

        # Afficher la grille de fond
        canvas.create_image(0, 0, anchor="nw", image=grille_theme)


        # Dessiner les lignes horizontales
        for j in range(lignes + 1):  # +1 pour inclure la dernière ligne
            canvas.create_line(
                0, j * taille_case + taille_case,  # Début de la ligne
                colonnes * taille_case, j * taille_case + taille_case,  # Fin de la ligne
                fill="black", width=2  # Couleur et épaisseur de la ligne
            )

        # Dessiner les lignes verticales
        for i in range(colonnes + 1):  # +1 pour inclure la dernière colonne
            canvas.create_line(
                i * taille_case, 0,  # Début de la ligne
                i * taille_case, (lignes + 1) * taille_case,  # Fin de la ligne
                fill="black", width=2  # Couleur et épaisseur de la ligne
            )

        # Dessiner les emplacements vides (ovales noirs)
        for i in range(colonnes):
            for j in range(lignes):
                canvas.create_oval(
                    i * taille_case + 10, j * taille_case + 10,
                    (i + 1) * taille_case - 10, (j + 1) * taille_case - 10,
                    fill="black"
                )

        # Dessiner les jetons
        for i in range(colonnes):
            for j in range(lignes):
                if grille[j][i] == 1:  # Joueur 1 (rouge)
                    canvas.create_image(
                        i * taille_case + taille_case // 2,
                        (lignes - j - 1) * taille_case + taille_case // 2,
                        image=jeton_joueur_1
                    )
                elif grille[j][i] == 2:  # Joueur 2 (image)
                    canvas.create_image(
                        i * taille_case + taille_case // 2,
                        (lignes - j - 1) * taille_case + taille_case // 2,
                        image=jeton_joueur_2
                    )



    #décalage pour l'instant en fonction de la taille grille mais a rendre modifiable

    # Alors j'ai pensé un peu au placement des jetons par clic, c'est pas encore ça + faut alterner les joueurs mieux mais l'idée est là
    # doc thinker event : https://docs.python.org/3/library/tkinter.html#bindings-and-events

    def ajouter_jeton(grille, col, J):
        for i in range(0, lignes):
            if grille[i][col] == 0:
                grille[i][col] = J
                break
        return grille


    def alternance_joueur(event, grille, taille_case, colonnes, cmpt):
        colonne_clique = event.x // taille_case  #position x de la souris donc la colonne choisie
        if colonne_clique >= colonnes:
            return grille, cmpt

        if cmpt % 2 == 0: 
            J = 1 #là sera rouge
        else:  
            J = 2 #là sera jaune 

        grille = ajouter_jeton(grille, colonne_clique, J)  
        tracer_grille(grille)  
        cmpt += 1 
        historique_coups.append(colonne_clique) 

        return grille, cmpt

    #pour gérer le nbr de clic/alternance
    def clic_canvas(event):
        global grille, cmpt
        colonne_clique = event.x // taille_case  # Déterminer la colonne cliquée
        if colonne_clique >= colonnes:
            return  # Si la colonne est invalide, ne rien faire

        # Déterminer le joueur actuel
        joueur = 1 if cmpt % 2 == 0 else 2

        # Ajouter le jeton dans la grille
        grille = ajouter_jeton(grille, colonne_clique, joueur)

        # Redessiner la grille
        tracer_grille(grille)

        # Incrémenter le compteur de tours
        cmpt += 1



    cmpt = 0 #début compteur

    canvas.bind("<Button-1>", clic_canvas)

    tracer_grille(grille)

    #Remettre a zero la grille à chaque ouverture de la fenetre :

    def reset_grille():
        global grille, cmpt, historique_coups
        grille = creation_grille()  
        cmpt = 0  # clic 0
        historique_coups.clear()  #pour éviter historique garde ancien coups
        tracer_grille(grille)
        message_label.config(text="Grille bien réinitialisée", font=("Comic Sans MS", 12, "bold"), fg = "#a97c11", bg = "#ffd88e")
        fenetre_grillejeux.after(3000, lambda: message_label.config(text="")) #j'ai mis 3s pour pas que ça reste infiniment 


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


    #Tous les bontons a afficher : 
    bouton_reset = tk.Button(frame_boutons, text="Reset", font=("Comic Sans MS", 10, "bold"), bg = "#a97c11", fg = "#ffd88e", command=reset_grille)
    bouton_reset.pack(side=tk.LEFT, padx=10)

    bouton_sauvegarder = tk.Button(frame_boutons, text="Sauvegarder", font=("Comic Sans MS", 10, "bold"), bg = "#a97c11", fg = "#ffd88e", command=sauvegarder_partie)
    bouton_sauvegarder.pack(side=tk.LEFT, padx=10)

    bouton_charger = tk.Button(frame_boutons, text="Charger", font=("Comic Sans MS", 10, "bold"), bg = "#a97c11", fg = "#ffd88e", command=charger_partie)
    bouton_charger.pack(side=tk.LEFT, padx=10)

    reset_grille()

    fenetre_grillejeux.mainloop()


###########################################################################################################################################
###########################################################################################################################################
# Code page d'accueil / Kinga

def f_fenetre_menu():

    # Création fenêtre accueil
    fenetre = tk.Tk()
    fenetre.title("Puissance-X")
    fenetre.geometry("1300x900")
    fenetre.state("zoomed")
    fenetre.configure(bg='#ffd88e')


    # On crée un label qui sera le nom du jeu
    nom_du_jeu = tk.Label(fenetre, text = "Puissance-X", font =("Copperplate", 100), fg = "#a97c11", bg = "#ffecaf")
    nom_du_jeu.place(relx=0.5, rely=0.25, anchor="center")

    # On crée le bouton "Jouer"
    bouton_jouer = tk.Button(fenetre, text ="Jouer", bg = "#a97c11", fg="#ffecaf", font=("Comic Sans MS", 25, "bold"), width = 10, height = 1, command = f_fenetre_nombre_joueur)
    bouton_jouer.place(relx=0.5, rely=0.55, anchor="center")

    # On crée le bouton "Paramètres"
    bouton_para = tk.Button(fenetre, text ="Paramètres", bg = "#a97c11", fg="#ffecaf", font=("Comic Sans MS", 9, "bold"), command = f_fenetre_parametres)
    bouton_para.place(relx=0.5, rely=0.7, anchor="center")

    bouton_règles = tk.Button(fenetre, text ="Règles du jeu", bg = "#a97c11", fg="#ffecaf", font=("Comic Sans MS", 9, "bold"), command = f_fenetre_regle)
    bouton_règles.place(relx=0.5, rely=0.77, anchor="center")

    # On affiche la fenêtre 
    fenetre.mainloop()

f_fenetre_menu()

###########################################################################################################################################
###########################################################################################################################################

