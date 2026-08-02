from models.livre import Livre
from models.etudiant import Etudiant
from models.emprunt import Emprunt

livre1 = Livre(
    1,
    "Python pour les SIG",
    "Mark Lutz"
)

etudiant1 = Etudiant(
    1,
    "Orlando",
    "orlando@gmail.com"
)

emprunt1 = Emprunt(
    1,
    etudiant1,
    livre1
)

print("===== LIVRE =====")
print(livre1.titre)
print(livre1.auteur)
print(livre1.disponible)

print()

print("===== ETUDIANT =====")
print(etudiant1.nom)
print(etudiant1.email)

print()

print("===== EMPRUNT =====")
print(emprunt1.etudiant.nom)
print(emprunt1.livre.titre)
print(emprunt1.date_emprunt)