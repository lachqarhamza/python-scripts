from Point import Point

def class:
    __premier = Point(0, 0)
    __deuxieme = Point(0, 0)
    __troisieme = Point(0, 0)

    def __init__(self, __premier, __deuxieme, __troisieme):
        self.__premier = __premier
        self.__deuxieme = __deuxieme
        self.__troisieme = __troisieme

    @property
    def __premier(self):
        return self.__premier

    @property
    def __deuxieme(self):
        return self.__deuxieme

    @property
    def __troisieme(self):
        return self.__troisieme

    @__premier.setter
    def __premier(self, value):
        self.__premier = value

    @__deuxieme.setter
    def __deuxieme(self, value):
        self.__deuxieme = value

    @__troisieme
    def __troisieme(self, value):
        self.__troisieme = value

   # def sont_alignes(self):
   #
