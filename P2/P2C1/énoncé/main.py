nombre1= input("Entrez votre premier nombre : ")
nombre2 = input("Entrez votre second nombre : ")

if not (nombre1.isnumeric() and nombre2.isnumeric()):
    print("L'une des valeurs entrées n'est pas un nombre. Veuillez entrer des nombres valides.  ")
    raise SystemExit("Fin du programme : Veuillez entrer des nombres valides.")
else :
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    operation = input("Entrez l'opération à effectuer (+, -, *, /) :")
    if operation != "+" and operation != "-" and operation != "*" and operation != "/" :
        raise SystemExit("Fin du programme : L'opérateur utilisé n'est pas reconnu.")
    else :
        match operation:
            case "+" :
                resultat = nombre1 + nombre2
                print(f"{nombre1} + {nombre2} = {resultat}")

            case "-" :
                resultat = nombre1 - nombre2
                print(f"{nombre1} - {nombre2} = {resultat}")

            case "*" :
                resultat = nombre1 * nombre2
                print(f"{nombre1} * {nombre2} = {resultat}")

            case "/" :
                if nombre2==0 :
                    raise SystemExit("Fin du programme : Divion par zéro impossible. ")
                else : 
                    resultat = nombre1 / nombre2
                    print(f"{nombre1} / {nombre2} = {round(resultat)}")

                    
