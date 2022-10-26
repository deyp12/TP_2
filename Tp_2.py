"""
Tp 2
Polashi Dey
406
description:Ce code est suppposé d'être un jeu de devinette,c'est à dire que joeur doit deviner le nombre choisi par hasard par le logiciel  """

import random



print("Bienvenue,Dans ce jeu,Il faut que vous devinez le nombre au aleratoire")



def jeu_devinette():

 """
Ce code va donner la choix au joeur d'avoir le nombre minimal et nombre maximale du nombre qu'il doit deviner,ainsi cela va donner le nombre de essais que le joueur
a prit de deviner et donner le choix de rejoueur ou de quitter à la fin du première partie du jeu
 """


    borne_minimale = int(input("C'est quoi le nombre minimale voulez vouz avoir dans ce jeu "))
    borne_maximale = int(input("C'est quoi le nombre maximale voulez vouz avoir dans ce jeu "))

    x = random.randint(borne_minimale, borne_maximale)

    nb_essai = 1
    print("Allons y")
    essai = int(input("entrez votre essai"))

    while essai != x:

        if essai > x:
            print("le nombre est plus petit")
            essai = int(input("entrez votre essai"))
            nb_essai = nb_essai + 1
        else:
            print("le nombre est plus grand")
            essai = int(input("entrez votre essai"))
            nb_essai = nb_essai + 1

    print("Bonne réponse!")
    print(f"vous avez dévinez en {nb_essai} essai")

    quit = (input("Voulez vous quitter?Répondez par oui ou non "))
    if quit == "oui":
        print("Au revoir")
    elif quit == "non":
        jeu_devinette()

jeu_devinette()
