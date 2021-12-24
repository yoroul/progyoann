# exo 20

# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]

# setl1 = set(liste_01)
# setl2 = set(liste_02)

# print(list(setl1.intersection(setl2)))

# # exo 21 : trier une liste de tupple sur le 2ème elt de chaque tupple
# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

# # Trier la liste ici
# liste.sort(key=lambda y : y[1])
# print(liste)

# # exo 22 : manipulation de dictionnaire
# employes = {"01": {"identite": {"Prenom": "Pierre", "nom": "Dupont"}}}
# print(employes["01"]['identite']['Prenom'])

# # la méthode get permet de revnoyer None si la clé n'existe pas ou spécifier une valeur par défaut (ici 1 dico vide {} ouun string 'valeur inconnue')
# print(employes.get("01", {}).get("identite", {}).get("Prenom", "valeur inconnue"))
# print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

# # exo 23 : additionner les valeurs d'un dico
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
# print(sum(employes.values()))

# # exo 24 : trouver l'erreur du module
# import random

# nombre_aleatoire = random.randint(0, 5)
# print(nombre_aleatoire)

# # exo 25 : rectifier une erreur de script
# # set permet d'éviter les doublons d'une liste
# liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

# resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
# # resultat = sorted(list(set(liste)))
# print(resultat)

# # exo 26 : importer une varibale d'un autre script
# from constants import nom

# print(nom)

# # exo 28 : chemin relatif du script et extensions
# import os
# print('le dossier parent', os.getcwd(),  '\nle chemin complet', __file__)

# fichier = "C:/Python36/python.exe"
# maliste = fichier.split('.')
# print(maliste[1])

# # autre solution avec splitext qui split les chemins relatifs
# print(os.path.splitext(fichier))
# print(os.path.splitext(fichier)[1].strip("."))

# # exo 29 : les variables d'environnement
# import os
# dico_var_envt = os.environ
# print([variables for variables in dico_var_envt.keys()])
# print(dico_var_envt.get('HOMEPATH'))

# # exo 30 : temps execution
# from time import time
    
# a = time()
# _ = [i*2 for i in range(9999999)]
# print(f"Temps d'exécution: {time() - a}s")

# from datetime import datetime
    
# a = datetime.now()
# _ = [i*2 for i in range(9999999)]
# print(f"Temps d'exécution: {datetime.now() - a}s")

# # exo 31 : 
# a = 0

# if a is not None:
# 	print(a)
# if type(a) is int:
#     print(type(a))

# # exo 32 - 33 - 34: manipulation chaine de caractères
# prenom = "Pierre"
# nom = "Dupont"
# print(f"Bonjour je m'appelle {prenom} {nom}")

# mot = "Udemy"
# reversed pour inverser, lower pour mettre en minuscule et capitalize pour mettre la 1ère lettre en majuscule
# print("".join([elt for elt in reversed(mot.lower())]).capitalize())
# print(mot[::-1].capitalize())

# import random
# mot = "Bonjour"
# print(''.join(random.sample(mot, k=len(mot))).capitalize())
# print(random.shuffle(list(mot)))

# # exo 35 :

# nombre = 2938.48872
# decimales = 3
# print(f"Nombre tronqué: {round(nombre,decimales)}")
# print(f"Nombre tronqué: {nombre:.{decimales}f}")

# # exo 36:
# a = 17
# print('vous êtes majeur!' if a > 18 else None)
# majeur = print('majeur!' if a > 18 else print('non majeur'))

# # exo 37 : age du chien
# age = float(input("quel est l'âge de votre chien (en années) : "))

# if age < 0:
#     print("l'âge doit être positif")
#     exit()
# elif age <= 2:
#     d_age = age * 10.5
# else:
#     d_age = 21 + (age - 2)*4
# print(f"l'âge adulte de votre chien est : {d_age} ans")

# # exo 38:
# a = 4
# b = 6
# c = 2
# milieu = a+b+c- min(a, b, c)- max(a,b,c)
# print(milieu)

# # exo 40 : boucles for
# mot = "Python"
# for i in mot:
#     print(mot.index(i), i)

# for i in range(len(mot)):
#     print(i)

# # exo 41 -42:

# def multiplicateur_mot(mult, mot):
# 	return mot * mult

# mot_multiplie = multiplicateur_mot(5, "Bonjour")
# print(mot_multiplie)

# def addition(a, b):
#     c = a + b
#     return c

# resultat = addition(5, 10)
# print(resultat)

# # exo 43 : tablede mutliplication

# nombre = 7
# def multiplication(nb):
#     for i in range(10):
#         res = nb * i
#         print(f"{i} * {nb} = {res}")

# multiplication(nombre)

# exo 44 : boucle for et enumerate (pour une liste pour récupérer l'indice) ; même principe que items() pour les dico
liste = ["Pierre", "Paul", "Marie"]
for i, elt in enumerate(liste):
    print(i, elt)