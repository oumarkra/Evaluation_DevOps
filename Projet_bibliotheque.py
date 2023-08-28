class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                print(f"Vous avez emprunté '{livre.titre}' par {livre.auteur}.")
                return
        print("Le livre n'est pas disponible pour l'emprunt.")

    def retourner_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and not livre.disponible:
                livre.disponible = True
                print(f"Vous avez retourné '{livre.titre}'. Merci !")
                return
        print("Ce livre n'appartient pas à cette bibliothèque ou il est déjà retourné.")

    def afficher_livres(self):
        print("Livres disponibles dans la bibliothèque:")
        for livre in self.livres:
            if livre.disponible:
                print(f"'{livre.titre}' par {livre.auteur}")
        print("\nLivres empruntés:")
        for livre in self.livres:
            if not livre.disponible:
                print(f"'{livre.titre}' par {livre.auteur}")

# Création de quelques livres
livre1 = Livre("Harry Potter et la Pierre Philosophale", "J.K. Rowling")
livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
livre3 = Livre("1984", "George Orwell")

# Création de la bibliothèque
bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Interaction avec la bibliothèque
bibliotheque.emprunter_livre("1984")
bibliotheque.emprunter_livre("Le Seigneur des Anneaux")
bibliotheque.retourner_livre("1984")

# Affichage des livres disponibles et empruntés
bibliotheque.afficher_livres()