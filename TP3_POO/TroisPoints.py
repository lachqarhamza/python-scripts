from Point import Point

class TroisPoints:
    __premier = Point(0, 0)
    __deuxieme = Point(0, 0)
    __troisieme = Point(0, 0)

    def __init__(self, __premier, __deuxieme, __troisieme):
        self.__premier = __premier
        self.__deuxieme = __deuxieme
        self.__troisieme = __troisieme

    @property
    def __premier(self):
        return self.___premier

    @property
    def __deuxieme(self):
        return self.___deuxieme

    @property
    def __troisieme(self):
        return self.___troisieme

    @__premier.setter
    def __premier(self, value):
        self.___premier = value

    @__deuxieme.setter
    def __deuxieme(self, value):
        self.___deuxieme = value

    @__troisieme.setter
    def __troisieme(self, value):
        self.___troisieme = value

    def sont_alignes(self):
        a = self.__premier.calculer_distance(self.__deuxieme)
        b = self.__premier.calculer_distance(self.__troisieme)
        c = self.__deuxieme.calculer_distance(self.__troisieme)
        if a == b + c or b == a + c or c == a + b:
            return True
        return False

    def est_isocele(self):
        a = self.__premier.calculer_distance(self.__deuxieme)
        b = self.__premier.calculer_distance(self.__troisieme)
        c = self.__deuxieme.calculer_distance(self.__troisieme)
        if a == b or a == c or c == b:
            return True
        return False
