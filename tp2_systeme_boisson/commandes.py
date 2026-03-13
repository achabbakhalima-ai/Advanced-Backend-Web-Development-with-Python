from fidelite import Fidelite

class Commande:

    def __init__(self, client):
        self.client = client
        self.boissons = []
    
    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        total= 0 
        for b in self.boissons:
            total += b.cout()
        return total
    def afficher(self):
        print("Client:", self.client.nom)
        for  b in self.boissons:
            print(b.description(), "-", b.cout(),"DH")
        print("Total:", self.prix_total(),"DH")

class CommandeSurPLace(Commande):
    def afficher(self):
        print("Commande sur place")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("Commande à emporter")
        super().afficher()

class CommandeFidelite(Commande, Fidelite):
    def valider(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)
