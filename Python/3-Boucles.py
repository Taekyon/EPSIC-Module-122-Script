## BOUCLES ##

# boucle for classique
# ici, une "range" de 4 à 10, en incrémant de 2 à 2
for i in range(4,10,2):
    print(i)

# # for i in range(10):
#     if i % 2 == 1:
#         continue
#     print(f"Bonjour {i}")

# Boucle foreach
# Création d'une liste de phiolosophe
philosophes = [ "Nietzsche", "Platon", "Kant", "Descartes" ]
# on parcourt tous Les éléments de La liste et on Les affiches
for philosophe in philosophes:
    print (f"Nom du philosophe :   {philosophe}")

