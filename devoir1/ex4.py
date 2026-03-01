print("1: addition")
print("2: soustraction")
print("3: multiplication")
print("4: division")
choix = input ("choisir une opération :")
if choix == "1" :
    a=int(input("entrer le premier nombre :"))
    b=int(input("entrer le dexième nombre :"))
    print("le résultat de l'addition est  :",a+b)
elif choix == "2" :
    a=int(input("entrer le premier nombre :"))
    b=int(input("entrer le dexième nombre :"))
    print("le résultat de la soustraction est  :",a-b)
elif choix == "3" :
    a=int(input("entrer le premier nombre :"))
    b=int(input("entrer le dexième nombre :"))
    print("le résultat de la miltiplication  est  :",a*b)
elif choix == "4" :
    a=int(input("entrer le premier nombre :"))
    b=int(input("entrer le dexième nombre :"))
    if b == 0 :
        print("division par zéro n'est pas autorisées")
    else :
        print("le résultat de la division  est  :",a/b)
else : 
    print("opération invalide")