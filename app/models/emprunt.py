from datetime import date

class Emprunt:

    def __init__(self, id, etudiant, livre):
        self.id = id
        self.etudiant = etudiant
        self.livre = livre
        self.date_emprunt = date.today()
        self.date_retour = None
