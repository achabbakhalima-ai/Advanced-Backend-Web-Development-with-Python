mdp_correct="python123"
mdp= input("entrer un mot de passe :")
while mdp != mdp_correct :
    print("mot de passe incorrect. essayer à nouveau.")
    mdp=input("entrer le mot de passe :")
print("mot de passe correct.Accès autorisé.")