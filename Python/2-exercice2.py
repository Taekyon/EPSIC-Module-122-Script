# TODO
# corriger le code pour pouvoir gérer les erreurs

# Exercice 2 #
print("EXERCICE 2")

annee = int(input("Entrez une année: "))
# Montre le type de la variable "annee"
print(type(annee))

if type(annee) is not int: # Test si la valeur entrée est un nombre entier
    print("la valeur entrée n'est pas valide")
# Test si l'année est bissextile
elif annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print("L'année ",annee," est bissextile")
# Résultat si non
else:
    print("L'année ",annee," n'est pas bissextile")