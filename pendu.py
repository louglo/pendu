#!/usr/bin/python

#fonction permettant de choisir élément randtestom d'une liste donnée
import random

banque = ["poulet","bidet","menthe","patate","cajou"]

guess = random.choice(banque)

mort = 0

historique = []

#join permet de display une liste sous forme de string
progres = []
for lettre in range(len(guess)):
    progres.append("_")

#outline = "_ " * len(guess)
#print ("Essaie de deviner le mot : " + outline)
print("Essaie de deviner le mot : " + " ".join(progres))
print("Si tu n'as pas trouvé au bout du 8ème essai... COUIC..!")

# test[0] au cas où des gens écrivent plusieurs lettres seule la première sera gardée
# on ne peut pas faire str + int donc on convertit tour en string avec str(tour)
while mort < 8:
    nul = 0
    print("")
    if mort == 7:
        print ("Attention dernière tentative")
    else:
        print ("Essai " + str(mort + 1))
    
    if historique != []:
        print("Les lettres que tu as proposé: " + ",".join(historique))

    test = input("Choisis une lettre: ").lower()
    while test in historique:
        print("Tu as déjà essayé la lettre " + test + "...\n")
        test = input("Choisis une lettre: ").lower()
    historique.append(test)
    print("Tu as proposé: " + "'" + test[0] + "'")
    print("Vérification...")

    # si juste guess à la place range() erreur à la ligne suivante pour "guess[lettre]" demande int:
    for lettre in range(len(guess)):
    #si bon, remplace le "_" par la lettre devinée
        if test[0] == guess[lettre]:
            progres[lettre] = test[0]
        else:
            nul = nul + 1

    #si nul < longueur du mot alors il y a eu des lettres découvertes à cette boucle
    if nul < len(guess):
        print ("Bien joué")
    else:
        mort = mort + 1
        print ("Raté")
    print (" ".join(progres))

    if "_" not in progres:
        print("Bravo tu as gagné!!!")
        quit()

print ("")
print ("Perdu!!!")
print ("Le mot était " + guess)
