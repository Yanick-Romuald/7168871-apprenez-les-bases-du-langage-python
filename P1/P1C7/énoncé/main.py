
# Écrivez votre code ici !


fruits = {"pomme":"rouge", "banane":"jaune", "orange":"orange"}
print(f"Le dictionnaire de fruits est : {fruits}")
fruits.items()

fruits['kiwi']="vert"
print(f"Le nouveau dictionnaire avec un élément de plus est : {fruits} ")

couleur_banane = fruits.get("banane")
print(f"La couleur de la banane est : {couleur_banane}")

fruits['pomme'] = "vert"

print(f"la nouvelle liste de fruits est : {fruits}")

del fruits["banane"]

print(f"la nouvelle liste de fruits est : {fruits}")

print(f"La liste des clés est la suivante : {fruits.keys()}")

