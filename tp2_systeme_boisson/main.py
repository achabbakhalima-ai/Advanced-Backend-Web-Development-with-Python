from boissons import Cafe, The
from decorateur_boisson import Lait, Sucre, Caramel
from commandes import CommandeFidelite
from client import Client

client= Client("Halima", 1, 0)

cafe = Cafe()
cafe = Lait(cafe)
cafe = Sucre(cafe)

the = The()
the = Caramel(the)

menu = cafe + the

commande = CommandeFidelite(client)

commande.ajouter_boisson(cafe)
commande.ajouter_boisson(the)
commande.ajouter_boisson(menu)

commande.afficher()

commande.valider()

print("Points de fidélité du client:", client.points)

