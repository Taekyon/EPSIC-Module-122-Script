# TODO
#

# # Exercice 3 #
# print("EXERCICE 3")
#
# nombre = int(input("Entrez un nombre: "))
# # Montre le type de la variable "nombre"
# print(type(nombre))
#
# if type(nombre) is not int: # Test si la valeur entrée est un nombre entier
#     print("la valeur entrée n'est pas valide")
# # Test si l'année est bissextile
# elif nombre % 4 == 0 and nombre % 100 != 0 or nombre % 400 == 0:
#     print("L'année ",nombre," est bissextile")
# # Résultat si non
# else:
#     print("L'année ",nombre," n'est pas bissextile")

# EXERCICE 1: Nombre premier
nombre = int(input("Entrez un nombre: "))

# Puissance de 0.5 == racine
racine = int(pow(nombre, 0.5))
# Stockage dans une variable
estPremier = True
print(f"Nombre {nombre}, racine {racine}")

if nombre < 2:
    estPremier = False

elif nombre > 2

for i in range(2, racine+1):
    print(f"Test avec i comme valeur: {i}")
    # Si on trouve une valeur de i qui divise le nombre, nombre est premier.
    if nombre % i == 0:
        print(f"Le nombre {nombre} n'est pas premier")
        estPremier = False
        break