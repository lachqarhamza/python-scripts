from Adresse import Adresse
from Personne import Personne
from ListePersonnes import ListePersonnes

# test of Adresse class
# creation of three addresses
a1 = Adresse("rue 1", "ville 1", "41000")
a2 = Adresse("rue 2", "ville 2", "42000")
a3 = Adresse("rue 3", "ville 3", "43000")

# preparation of a list of addresses
adresses = []
adresses.append(a1)
adresses.append(a2)
adresses.append(a3)

# test of Personne class
# creation of a list of type personne
p1 = Personne("Hakima", "F", adresses)
p2 = Personne("Hamza", "M", adresses)
p3 = Personne("Salma", "F", adresses)
p4 = Personne("Ayoub", "M", adresses)
p5 = Personne("Amal", "F", adresses)

personnes = []
personnes.append(p1)
personnes.append(p2)
personnes.append(p3)
personnes.append(p4)
personnes.append(p5)

# test of ListePersonnes class

# test the constructor
lp = ListePersonnes(personnes)

# test find_by_nom function
print("---- test find_by_nom ----")
print("name exist: ", lp.find_by_nom("Hakima"))
#print("name doesn't exist: ", lp.find_by_nom("Mourad"))

# test exists_code_postal function
#print("---- test exists_code_postal ----")
#print("pc exist", lp.exists_code_postal("43000"))
#print("pc doesn't exist", lp.exists_code_postal("555"))

