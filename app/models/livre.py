class Livre:

    def __init__(self, id, titre, auteur):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print("Ce livre est déjà emprunté.")

    def retourner(self):
        self.disponible = True
        print(f"Le livre '{self.titre}' a été retourné.")