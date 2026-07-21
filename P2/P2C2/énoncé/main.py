# Ecrivez votre code ici !

nombres = input("Entrez votre liste de nombre séparés par des virgules")
liste = nombres.strip().split(",")
liste_entiers = []
somme = 0
for i in liste :
  liste_entiers.append(int(i))

for i in liste_entiers :
  somme += i

print(f"La somme des nombres entrés est {somme}")
