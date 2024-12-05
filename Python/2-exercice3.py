# TODO
#

# Exercice 3 #
print("EXERCICE 3")

nombre = int(input("Entrez un nombre: "))
# Montre le type de la variable "nombre"
print(type(nombre))

if type(nombre) is not int: # Test si la valeur entrée est un nombre entier
    print("la valeur entrée n'est pas valide")
# Test si l'année est bissextile
elif nombre % 4 == 0 and nombre % 100 != 0 or nombre % 400 == 0:
    print("L'année ",nombre," est bissextile")
# Résultat si non
else:
    print("L'année ",nombre," n'est pas bissextile")