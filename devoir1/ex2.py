contacts = []
while True:
    print("1.Ajouter un contact")
    print("2.afficher tous les contacts")
    print("3.quitter le programme")
    choix = input("choisir une option : ")
    if choix == "1":
        nom = input("entrer le nom du contact : ")
        telephone = input("entrer le telephone du contact : ")
        contacts.append((nom, telephone))
        print("contact ajouté avec succès")
    elif choix == "2":
        if len(contacts) == 0:
            print("Aucun contact dans le carnet.")
        else:
            print("\nListe des contacts :")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact}")
        
    elif choix == "3":
        break
    else:
        print("option invalide")