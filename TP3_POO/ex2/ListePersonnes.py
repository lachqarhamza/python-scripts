class ListePersonnes:
    def __init__(self, __personnes):
        self.__personnes = __personnes

    @property
    def __personnes(self):
        return self.__personnes

    @__personnes.setter
    def __personnes(self, value):
        self.__personnes = value

    def find_by_nom(self, s):
        for p in self.__personnes:
            if p.__nom == s:
                return p
        return None

    def exists_code_postal(self, cp):
        for p in self.__personnes:
            for a in p.__adresses:
                if a.__code_postal == cp:
                    return True
        return False

