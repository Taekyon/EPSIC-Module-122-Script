## BOUCLES ##

# # boucle for classique
# # ici, une "range" de 4 à 10, en incrémant de 2 à 2
# for i in range(4,10,2):
#     print(i)
#
# # for i in range(10):
#     if i % 2 == 1:
#         continue
#     print(f"Bonjour {i}")
# # Boucle foreach
# # Création d'une liste de philosophe
# philosophes = [ "Nietzsche", "Platon", "Kant", "Descartes" ]
# # on parcourt tous Les éléments de La liste et on Les affiches
# for philosophe in philosophes:
#     print (f"Nom du philosophe :   {philosophe}")

# Exercice 1
# Créer un script pour convertir une valeur décimal en binaire.
nbr = int(input("Entrez le nombre à convertir :"))
binaire = 0
# # Définir l'incrément
# # NE MARCHE PAS, TROP COMPLEXE
# i = 0
# while i < nbr:
#     i += 1
#     print(i)
#     if i % 2 == 1:
#         resultat += 1


# TODO
# trouver comment append
while nbr > 0:
    nbr /= 2
    print(f"décimal = {nbr}")
    if nbr % 2 == 1:
        nbr -= 1
        print(nbr)
        continue
