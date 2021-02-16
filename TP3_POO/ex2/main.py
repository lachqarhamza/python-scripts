from Adresse import Adresse
from Personne import Personne
from ListePersonnes import ListePersonnes

# test of Adresse class
# creation of three addresses
a1 = Adresse("rue 1", "ville 1", "41000")
a2 = Adresse("rue 2", "ville 2", "42000")
a3 = Adresse("rue 3", "ville 3", "43000")
a4 = Adresse("rue 3", "ville 7", "43000")

# preparation of a list of addresses
adresses = []
adresses.append(a1)
adresses.append(a2)
adresses.append(a3)

adresses2 = []
adresses2.append(a4)

# test of Personne class
# creation of a list of type personne
p1 = Personne("name 1", "F", adresses)
p2 = Personne("name 2", "M", adresses)
p3 = Personne("name 3", "F", adresses)
p4 = Personne("name 4", "M", adresses)
p5 = Personne("name 5", "F", adresses2)

personnes = []
personnes.append(p1)
personnes.append(p2)
personnes.append(p3)
personnes.append(p4)

personnes3 = []
personnes3.append(p5)
personnes3.append(p5)
personnes3.append(p5)

personnes4 = []
personnes4.append(p4)
personnes4.append(p5)

# test of ListePersonnes class

# test the constructor
lp = ListePersonnes(personnes)
lp3 = ListePersonnes(personnes3)

# test find_by_nom function
print("---- test find_by_nom ----")
print("name exist: ", lp.find_by_nom("name 1"))
print("name doesn't exist: ", lp.find_by_nom("Mourad"))

#test exists_code_postal function
print("---- test exists_code_postal ----")
print("pc exist: ", lp.exists_code_postal("43000"))
print("pc doesn't exist: ", lp.exists_code_postal("555"))

# test count_Personne_ville
print("ville exist: ", lp.count_personne_ville("ville 1"))
print("ville doesn't exist: ", lp.count_personne_ville("ville 8"))
print("ville exist once: ", lp3.count_personne_ville("ville 7"))

# test edit personne nom

# check before the change
print("------ before -----------")
for p in lp.personnes:
    print(p.nom)

# make a change
lp.edit_personne_nom("name 1", "name 111")

# check after the change
print("------- after -------")
for p in lp.personnes:
    print(p.nom)

# test edit_personne_ville
lp4 = ListePersonnes(personnes4)
print("-------- befor ------------")
for p in lp4.personnes:
    print(p.nom + "---")
    for a in p.adresses:
        print(a.ville)
lp4.edit_personne_ville("name 4", "ville 111")
print("----------- after ------------")
for p in lp4.personnes:
    print(p.nom + "----")
    for a in p.adresses:
        print(a.ville)
