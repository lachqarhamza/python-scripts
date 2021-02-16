class ListePersonnes:
    def __init__(self, __personnes):
        self.__personnes = __personnes

    @property
    def personnes(self):
        return self.__personnes

    @personnes.setter
    def personnes(self, value):
        self.__personnes = value

    def find_by_nom(self, s):
        for p in self.personnes:
            if p.nom == s:
                return p
        return None

    def exists_code_postal(self, cp):
        for p in self.personnes:
            for a in p.adresses:
                if a.code_postal == cp:
                    return True
        return False

    def count_personne_ville(self, ville):
        count = 0
        for p in self.personnes:
            for a in p.adresses:
                if a.ville == ville:
                    count += 1
                    break
        return count

    def edit_personne_nom(self, oldNom, newNom):
        for p in self.personnes:
            if p.nom == oldNom:
                p.nom = newNom

    def edit_personne_ville(self, nom, newVille):
        for p in self.personnes:
            if p.nom == nom:
                for a in p.adresses:
                    a.ville = newVille
