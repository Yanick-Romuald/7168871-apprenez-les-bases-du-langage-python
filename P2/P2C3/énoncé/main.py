# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel) :
    saMe = salaire_annuel / 12
    return saMe

def salaire_hebdomadaire(salaire_mensuel) :
    saHe = salaire_mensuel / 4
    return saHe

def salaire_horaire(salire_hebdomadaire, heures_travaillees) :
    saHo = salire_hebdomadaire / heures_travaillees
    return saHo

salaire_annuel=float(input("Entrez votre salaire annuel : "))

heuresTravaillees = int(input("Entrez le nombre d'heures travaillées par semaine : "))

print(f"Votre salaire horaire est de : {round(salaire_horaire(salaire_hebdomadaire(salaire_mensuel(salaire_annuel)), heuresTravaillees),2)} euros")
